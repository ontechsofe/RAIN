<template>
    <v-container>
        <v-layout column>
            <v-flex class="mb-3">
                <v-card>
                    <v-card-media>
                        <v-sheet color="transparent">
                            
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
    const gradients = [
        ['#222'],
        ['#42b3f4'],
        ['red', 'orange', 'yellow'],
        ['purple', 'violet'],
        ['#00c6ff', '#F0F', '#FF0'],
        ['#f72047', '#ffd200', '#1feaea']
    ]

    export default {
        name: "Home",
        data: () => ({
            gradient: gradients[5],
            value: [0, 2, 5, 9, 5, 10, 3, 5, 0, 0, 1, 8, 2, 9, 0],
            gradientDirection: 'top'
        })
    }
</script>

<style scoped>

</style>
