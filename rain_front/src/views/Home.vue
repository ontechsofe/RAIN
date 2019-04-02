<template>
    <v-container>
        <v-layout column>
            <v-flex class="mb-3">
                <v-card>
                    <v-card-media>
                        <v-sheet color="transparent">
                            <vue-chart :data="lineGraph.chartData" :options="lineGraph.options" type="line"></vue-chart>
                        </v-sheet>
                    </v-card-media>
                    <v-card-text></v-card-text>     
                </v-card>
            </v-flex>
            <v-flex class="mb-3">
                <v-card>
                    <v-card-media>
                        <v-sheet color="transparent">
                            <v-sparkline 
                            :value="value"
                            :gradient="gradient"
                            :smooth="10"
                            :padding="8"
                            :line-width="2"
                            stroke-linecap="round"
                            gradient-direction="top"
                            auto-draw
                            ></v-sparkline>
                        </v-sheet>
                    </v-card-media>
                    <v-card-text></v-card-text>     
                </v-card>
            </v-flex>
        </v-layout>
    </v-container>
</template>

<script>
    import axios from 'axios'
    import moment from 'moment-timezone'

    const sortEpoch = (a, b) => {
        return a.date_value - b.date_value
    }

    const gradients = [
        ['#222'],
        ['#42b3f4'],
        ['red', 'orange', 'yellow'],
        ['purple', 'violet'],
        ['#00c6ff', '#F0F', '#FF0'],
        ['#f72047', '#ffd200', '#1fa8ea']
    ]

    export default {
        name: "Home",
        data: () => ({
            gradient: gradients[5],
            value: [],
            gradientDirection: 'top',
            currentTemp: 0,
            currentDew: 0,
            lineGraph: {
                chartData: {
                    labels: [0],
                    datasets: [{
                        fill: false,
                        backgroundColor: '#FF0',
                        borderColor: '#1fa8ea',
                        data: [],
                    }]
                },
                options: {
                    responsive: true,
                    title: {
                        display: false,
                    },
                        legend: {
                        display: false,
                        position: 'bottom'
                    },
                    tooltips: {
                        mode: 'index',
                        intersect: false,
                    },
                    hover: {
                        mode: 'nearest',
                        intersect: true
                    },
                    scales: {
                        xAxes: [{
                            display: true,
                            scaleLabel: {
                                display: true,
                                labelString: 'Hour'
                            }
                        }],
                        yAxes: [{
                            display: true,
                            scaleLabel: {
                                display: true,
                                labelString: 'Temp'
                            }
                        }]
                    }
                }
            }

        }),
        mounted() {
            let c = this
            c.loaded = true
            let now = moment().minute(0).second(0).millisecond(0).valueOf() 
            let startOfToday = moment().hour(0).minute(0).second(0).millisecond(0).valueOf()
            axios.get('http://sofe3720.ml:8000/forecast').then(response => {
                let res = response.data.data
                c.value = []
                res.sort(sortEpoch).forEach(element => {
                    c.value.push(element.predicted.temp)
                    let dt = moment(element.date_value).tz("America/Toronto").format("HH:mm")
                    c.lineGraph.chartData.labels.push(dt)
                    c.lineGraph.chartData.datasets[0].data.push(element.predicted.temp)
                    // console.log("Element:", element.date_value, "Now:", now)
                })
                c.loaded = true
            }).catch(error => {
                console.error(error)
            }) 
        }
    }
</script>

<style scoped>

</style>
