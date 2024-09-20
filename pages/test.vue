// pages/test.vue
<template>
  <div>
    <h1>{{ name }}</h1>
  </div>
</template>

<script>
import { useStore } from 'vuex';

export default {
  setup() {
    const store = useStore();
    return {
      name: store.state.name,
    };
  },
};
</script>