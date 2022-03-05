<template>
  <div id="app">
    <Header />
    <router-view />
    <Footer />
  </div>
</template>

<script>
import Header from "@/pages/Header";
import Footer from "@/pages/Footer";

export default {
  name: "header",
  components: {
    Header,
    Footer,
  },
};
</script>
