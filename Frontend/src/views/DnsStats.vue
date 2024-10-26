<template>
    <div class="w-full min-h-screen">
        <h1 class="text-2xl font-semibold">BIND Dns Stats</h1>
        <TopDomainTable/>
    </div>
</template>

<script>
import TopDomainTable from '@/components/topDomainTable.vue';

export default {
    components: {
        TopDomainTable,
    }
}
</script>