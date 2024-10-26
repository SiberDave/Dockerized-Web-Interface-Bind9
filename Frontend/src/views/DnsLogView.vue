<template>
  <div >
    <h1 class="text-2xl text-center font-semibold">BIND DNS History Log</h1>
    <DnsTrafficTable/>
  </div>
</template>

<script>

import DnsTrafficTable from '../components/Dns-trafficTable.vue';

export default {
  components: {
    DnsTrafficTable,
  }
}

</script>