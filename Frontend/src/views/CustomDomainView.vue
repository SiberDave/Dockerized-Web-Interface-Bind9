<template>
    <div class="w-full h-full">
      <h1 class="text-2xl">Custom Domain List</h1>
      <CustomDomainForm/>
      <CustomDomainComponentVue ref="customDomainTable" />
    </div>
</template>
  
<script>
import CustomDomainComponentVue from "@/components/CustomDomainComponent.vue";
import CustomDomainForm from "@/components/CustomDomainForm.vue";

export default {
    components: {
    CustomDomainComponentVue,
    CustomDomainForm,
    }
}
</script>