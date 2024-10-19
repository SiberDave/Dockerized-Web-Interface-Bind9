<template>
    <div class="w-full h-full">
      <h1 class="text-2xl">Custom Domain List</h1>
      <DomainBlockFormVue/>
      <CustomDomainComponentVue ref="domainBlockTable" />
    </div>
</template>
  
<script>
import CustomDomainComponentVue from "@/components/CustomDomainComponent.vue";
import DomainBlockFormVue from "@/components/DomainBlockForm.vue"

export default {
    components: {
    CustomDomainComponentVue,
    DomainBlockFormVue,
    }
}
</script>