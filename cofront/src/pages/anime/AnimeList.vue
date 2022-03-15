<template>
  <n-space style="width: 100%" align="center" justify="center"> </n-space>
</template>

<script>
import { client } from "@/axios";
import { parseResponseException } from "@/utils";

export default {
  name: "AnimeList",
  data() {
    return {
      page: 1,
      anime: [],
      animeCount: 0,
      animePerPage: 12,
    };
  },
  async mounted() {
    try {
      const response = await client.get("/anime/", {
        params: this.$route.query,
      });
      this.anime = response.data.results;
      this.animeCount = response.data.count;
      this.animePerPage = this.anime.length;
    } catch (e) {
      this.notification.error({
        title: "Данные не были получены!",
        content: parseResponseException(e),
        duration: 10000,
      });
    }
  },
  methods: {},
};
</script>

<style scoped></style>
