<template>
    <div class="w-full grid grid-cols-5">
        <div class="w-full"/>
        <div class="col-span-3">
            <button id="addbutton" @click="openmodal()" class="py-1 px-2 bg-green-300 mt-2 rounded-md">Add Custom Domain</button>
            <div id="div-modal" class="py-3 insert-div mt-2 rounded-md" style="background-color: #d8d8d8">
                <form @submit.prevent="add_domain_block" method="post">
                    <div class="w-full grid grid-cols-3">
                        <div class="w-full col-span-3 flex">
                            <div class="w-full">
                                <label for="domain_field" class="text-s">Domain</label><br>
                                <input type="text" v-model="domaindata.domain" id="domain_field" class="w-4/5">
                            </div>
                        </div>
                        <div class="w-full col-span-3 flex flex-col justify-center items-center">
                            <div class="w-full">
                                <label for="ip_field" class="text-s">IP Address</label><br>
                                <input type="text" v-model="domaindata.ip" id="ip_field" class="w-4/5">
                            </div>
                        </div>
                        <div class="col-span-3 py-3">
                            <button class="border bg-green-400 px-2 py-1 " type="submit">Submit</button>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'

    export default {
        data(){
            return {
                domaindata: {
                    domain: '',
                    ip: ''
                }
            }
        },
        methods: {
            openmodal() {
                var modal = document.getElementById('div-modal')
                modal.style.display = (modal.style.display === 'none' || modal.style.display === '') ? 'block' : 'none'
            },
            add_domain_block() {
                if (this.domaindata.domain.length <= 0){
                    alert("Input cant be Empty")
                }
                else {
                    axios.post(`http://${process.env.VUE_APP_HOST_API}:3000/add-custom-domain`, this.domaindata)
                    .then(response => {
                        var modal = document.getElementById('div-modal')
                        modal.style.display = 'none'
                        alert(response.data)
                        this.domaindata.domain = ''
                        this.domaindata.ip = ''
                        this.$parent.$refs.customDomainTable.fetchData()
                    })
                    .catch(error => {
                        alert(error)
                    })
                }
                
            }
        }
    }
</script>

<style scoped>
    .label-input{
        padding-left: calc(10%);
    }
    .insert-div{
        display: none;
    }
</style>