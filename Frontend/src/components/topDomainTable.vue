<template>
    <div class="w-full h-auto snap-y snap-mandatory">
        <div class="w-full my-1 flex flex-row justify-left">
            <select v-model="time" id="type" class="w-1/5 text-center ms-10">
                <option value="60m">60 Minutes</option>
                <option value="1d">1 Days</option>
                <option value="1m">1 Months</option>
                <option value="1y">1 Year</option>
                <option value="all">All time</option>
            </select>
        </div>
        <div class="w-full h-auto snap-center">
            <div class="w-full font-semibold">
                <h1 v-if="time == '60m'" class="text-center py-5 text-xl text-white">Top All Domain Request Last 60 Min</h1>
                <h1 v-else-if="time == '1d'" class="text-center py-5 text-xl text-white">Top All Domain Request Last 1 Day</h1>
                <h1 v-else-if="time == '1m'" class="text-center py-5 text-xl text-white">Top All Domain Request Last 1 Month</h1>
                <h1 v-else-if="time == '1y'" class="text-center py-5 text-xl text-white">Top All Domain Request Last 1 Year</h1>
                <h1 v-else-if="time == 'all'" class="text-center py-5 text-xl text-white">Top All Domain Request</h1>
            </div>
            <div class="w-full h-full flex flex-row justify-center">
                <div class="p-5 opacity-75 rounded-md" style="width: 45%; background-color: white;" >
                    <canvas id="all_domain_stats"></canvas>
                </div>
            </div>
        </div>
        <div class="w-full h-auto snap-center mb-5">
            <div class="w-full col-span-2 font-semibold">
                <h1 v-if="time == '60m'" class="text-center py-5 text-xl text-white">Top Success Domain Request Last 60 Min</h1>
                <h1 v-else-if="time == '1d'" class="text-center py-5 text-xl text-white">Top Success Domain Request Last 1 Day</h1>
                <h1 v-else-if="time == '1m'" class="text-center py-5 text-xl text-white">Top Success Domain Request Last 1 Month</h1>
                <h1 v-else-if="time == '1y'" class="text-center py-5 text-xl text-white">Top Success Domain Request Last 1 Year</h1>
                <h1 v-else-if="time == 'all'" class="text-center py-5 text-xl text-white">Top Success Domain Request</h1>
            </div>
            <div class="w-full h-full flex flex-row justify-center">
                <div class="p-5 opacity-75 rounded-md" style="width: 45%; background-color: white;" >
                    <canvas id="success_domain_stats"></canvas>
                </div>
            </div>
        </div>
        <div class="w-full h-auto snap-center mb-5">
            <div class="w-full col-span-2 font-semibold">
                <h1 v-if="time == '60m'" class="text-center py-5 text-xl text-white">Top Blocked Domain Request Last 60 Min</h1>
                <h1 v-else-if="time == '1d'" class="text-center py-5 text-xl text-white">Top Blocked Domain Request Last 1 Day</h1>
                <h1 v-else-if="time == '1m'" class="text-center py-5 text-xl text-white">Top Blocked Domain Request Last 1 Month</h1>
                <h1 v-else-if="time == '1y'" class="text-center py-5 text-xl text-white">Top Blocked Domain Request Last 1 Year</h1>
                <h1 v-else-if="time == 'all'" class="text-center py-5 text-xl text-white">Top Blocked Domain Request</h1>
            </div>
            <div class="w-full h-full flex flex-row justify-center">
                <div class="p-5 opacity-75 rounded-md" style="width: 45%; background-color: white;" >
                    <canvas id="blocked_domain_stats"></canvas>
                </div>
            </div>
        </div>
        <div class="w-full h-auto snap-center mb-5">
            <div class="w-full font-semibold">
                <h1 v-if="time == '60m'" class="text-center py-5 text-xl text-white">Top Failed Domain Request Last 60 Min</h1>
                <h1 v-else-if="time == '1d'" class="text-center py-5 text-xl text-white">Top Failed Domain Request Last 1 Day</h1>
                <h1 v-else-if="time == '1m'" class="text-center py-5 text-xl text-white">Top Failed Domain Request Last 1 Month</h1>
                <h1 v-else-if="time == '1y'" class="text-center py-5 text-xl text-white">Top Failed Domain Request Last 1 Year</h1>
                <h1 v-else-if="time == 'all'" class="text-center py-5 text-xl text-white">Top Failed Domain Request</h1>
            </div>
            <div class="w-full h-full flex flex-row justify-center">
                <div class="p-5 opacity-75 rounded-md" style="width: 45%; background-color: white;" >
                    <canvas id="failed_domain_stats"></canvas>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
    import Chart from 'chart.js/auto'
    import axios from 'axios'

    let all_domain_graph = null
    let success_domain_graph = null
    let blocked_domain_graph = null
    let failed_domain_graph = null

    export default {
        data() {
            return {
                all_domain: [],
                success_domain: [],
                blocked_domain: [],
                failed_domain: [],
                time: '60m',
            }
        },
        mounted() {
            this.initialize()
        },
        watch: {
            time() {
                this.updateChart()
            }
        },
        methods: {
            async fetchQuery(type){
                let response = await axios.get(`http://${process.env.VUE_APP_HOST_API}:3000/get-top-query/${type}/${this.time}`)
                return response.data
            },
            async getTopDomain(){
                this.all_domain = await this.fetchQuery('all')
                this.success_domain = await this.fetchQuery('queries')
                this.blocked_domain = await this.fetchQuery('rpz')
                this.failed_domain = await this.fetchQuery('query-errors')
            },
            async generate_chart(id,datalist){
                const data = datalist
                let element = document.getElementById(id)

                return new Chart(
                    element,
                    {
                        type:'pie',
                        data: {
                            labels: data.map(row => row.domain),
                            datasets: [{
                                data: data.map(row => row.count),
                                backgroundColor: [
                                    'rgb(89, 31, 197)',
                                    'rgb(31, 197, 60)',
                                    'rgb(197, 31, 194)',
                                    'rgb(115, 66, 34)',
                                    'rgb(243, 159, 24)',
                                    'rgb(74, 25, 44)',
                                    'rgb(117, 092, 72)',
                                    'rgb(255, 255, 0)',
                                    'rgb(228, 160, 16)',
                                    'rgb(28, 28, 28)',
                                ]
                            }],
                        },
                        options: {
                            responsive: true,
                            plugins: {
                                legend: {
                                    position: 'top',
                                    fullSize: false,
                                    labels: {
                                        boxHeight: 8 ,
                                        font: {
                                            size: 12
                                        }
                                    }
                                },
                                customCanvasBackgroundColor: {
                                    color: 'White',
                                }
                            },
                            layout: {
                                padding: {
                                    bottom: 0
                                }
                            }
                        }
                    }
                )
            },
            async initialize(){
                await this.getTopDomain()

                try {
                    if (this.all_domain.length > 0) all_domain_graph = await this.generate_chart("all_domain_stats",this.all_domain)
                    if (this.success_domain.length > 0) success_domain_graph = await this.generate_chart("success_domain_stats",this.success_domain)
                    if (this.blocked_domain.length > 0) blocked_domain_graph = await this.generate_chart("blocked_domain_stats",this.blocked_domain)
                    if (this.failed_domain.length > 0) failed_domain_graph = await this.generate_chart("failed_domain_stats",this.failed_domain)
                } catch (error) {
                    console.error("Error when creating Chart, Please refresh the page, Error Message : " + error)
                }
            },
            updateData(graph,graph_data) {
                graph.data.datasets[0].data = graph_data.map(row => row.count)
                graph.data.labels = graph_data.map(row => row.domain)
                graph.update()
            },
            async updateChart() {
                await this.getTopDomain()
                
                if (all_domain_graph != null){
                    if (this.all_domain.length > 0) this.updateData(all_domain_graph,this.all_domain)
                    else{
                        all_domain_graph.destroy()
                        all_domain_graph = null
                    }
                }
                else all_domain_graph = await this.generate_chart("all_domain_stats",this.all_domain)

                if (success_domain_graph != null){
                    if (this.success_domain.length > 0) this.updateData(success_domain_graph,this.success_domain)
                    else {
                        success_domain_graph.destroy()
                        success_domain_graph = null
                    }
                }
                else success_domain_graph = await this.generate_chart("success_domain_stats",this.success_domain)

                if (blocked_domain_graph != null){
                    if (this.blocked_domain.length > 0) this.updateData(blocked_domain_graph,this.blocked_domain)
                    else{
                        blocked_domain_graph.destroy()
                        blocked_domain_graph = null
                    }
                }
                else blocked_domain_graph = await this.generate_chart("blocked_domain_stats",this.blocked_domain)

                if (failed_domain_graph != null){
                    if (this.failed_domain.length > 0) this.updateData(failed_domain_graph,this.failed_domain)
                    else{
                        failed_domain_graph.destroy()
                        failed_domain_graph = null
                    }
                }
                else failed_domain_graph = await this.generate_chart("failed_domain_stats",this.failed_domain)
            }
        }
    }
</script>
<style scoped>
thead {
    background-color: #413f54; 
    color: white;
}

tbody tr:nth-of-type(even) {
    background-color: rgb(206, 206, 206);
}
</style>