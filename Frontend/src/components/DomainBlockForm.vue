<template>
    <div class="w-full grid grid-cols-5">
        <div class="w-full"/>
        <div class="col-span-3">
            <button id="addbutton" @click="openmodal()" class="py-1 px-2 bg-green-300 mt-2 rounded-md">Add Domain Block</button>
            <div id="div-modal" class="py-3 insert-div mt-2 rounded-md" style="background-color: #d8d8d8">
                <form @submit.prevent="add_domain_block" method="post">
                    <div class="w-full grid grid-cols-3">
                        <div class="w-full col-span-3 flex">
                            <div class="w-full">
                                <label for="domain_field" class="text-s">Domain</label><br>
                                <input type="text" v-model="domaindata.domain" id="domain_field" class="w-4/5 px-1">
                            </div>
                        </div>
                        <div class="w-full col-span-3 flex flex-col justify-center items-center">
                            <label for="record" class="text-s">Record Type</label>
                            <select v-model="domaindata.record" id="record" class="w-4/5 py-1 text-center">
                                <option value="A">A</option>
                                <option value="AAAA">AAAA</option>
                                <option value="CNAME">CNAME</option>
                            </select>
                        </div>
                        <div class="w-full col-span-3 flex flex-col justify-center items-center">
                            <div class="w-full">
                                <label for="note_field" class="text-s">Note</label><br>
                                <input type="text" v-model="domaindata.note" id="note_field" class="w-4/5 px-1">
                            </div>
                        </div>
                        <div class="col-span-3 py-3">
                            <button class="border bg-green-400 px-2 py-1 " type="submit">Submit</button>
                        </div>
                    </div>
                </form>
            </div>
            <br/>
            <button id="addbatchbutton" @click="openbatchmodal()" class="py-1 px-2 bg-green-300 mt-2 rounded-md">Add Domain Block from List</button>
            <div id="div-modal-batch" class="py-3 insert-div mt-2 rounded-md" style="background-color: #d8d8d8">
                <form @submit.prevent="add_batch_domain_block" method="post">
                    <div class="w-full grid grid-cols-3">
                        <div class="w-full col-span-3 flex">
                            <div class="w-full">
                                <label for="url_block" class="text-s">Host Block URL</label><br>
                                <input type="text" v-model="batchurl.url" id="url_block" class="w-4/5 px-1">
                            </div>
                        </div>
                        <div class="w-full col-span-3 flex flex-col justify-center items-center">
                            <label for="record" class="text-s">Record Type</label>
                            <select v-model="batchurl.record" id="record" class="w-4/5 py-1 text-center">
                                <option value="A">A</option>
                                <option value="AAAA">AAAA</option>
                                <option value="CNAME">CNAME</option>
                            </select>
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
                    record:'A',
                    note: ""
                },
                batchurl: {
                    url: '',
                    record: 'A'
                }
            }
        },
        methods: {
            openmodal() {
                var modal = document.getElementById('div-modal')
                var othermodal = document.getElementById('div-modal-batch')
                if (modal.style.display === 'none' || modal.style.display === ""){
                    modal.style.display = 'block'
                    othermodal.style.display = 'none'
                }
            },
            openbatchmodal(){
                var modal = document.getElementById('div-modal-batch')
                var othermodal = document.getElementById('div-modal')
                if (modal.style.display === 'none' || modal.style.display === ""){
                    modal.style.display = 'block'
                    othermodal.style.display = 'none'
                }
            },
            add_batch_domain_block() {
                if (this.batchurl.url.length <= 0) alert("Input cant be Empty")
                else{
                    this.$parent.$refs.domainBlockTable.checkloading()
                    axios.post(`http://${process.env.VUE_APP_HOST_API}:3000/add-batch-dns-block`, this.batchurl)
                    .then(response => {
                        var modal = document.getElementById('div-modal-batch')
                        modal.style.display = 'none'
                        this.$parent.$refs.domainBlockTable.checkloading()
                        alert(response.data)
                        this.batchurl.url = ''
                        this.batchurl.record = 'A'
                        this.$parent.$refs.domainBlockTable.fetchData()
                    })
                }
            },
            add_domain_block() {
                if (this.domaindata.domain.length <= 0) alert("Input cant be Empty")
                else {
                    axios.post(`http://${process.env.VUE_APP_HOST_API}:3000/add-dns-block`, this.domaindata)
                    .then(response => {
                        var modal = document.getElementById('div-modal')
                        modal.style.display = 'none'
                        alert(response.data)
                        this.domaindata.domain = ''
                        this.domaindata.record = 'A'
                        this.domaindata.note = ""
                        this.$parent.$refs.domainBlockTable.fetchData()
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