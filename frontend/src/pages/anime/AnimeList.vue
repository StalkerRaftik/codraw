<template>
  <n-space vertical>
    <n-space
        style="margin-top: 16px; margin-bottom: 16px; gap: 16px; width: 95vw;"
        justify="center"
    >
      <AnimeListCard
          v-for="(animeKey, iterKey) in cardsKeysArray"
          style="width: 300px; height: 500px;"
          :key="iterKey"
          :anime="animes[animeKey]"
      />
    </n-space>
    <n-space justify="center" style="margin-bottom: 24px">
      <n-pagination
          v-model:page="page"
          :page-count="Math.ceil(animeCount / animePerPage)"
          :page-slot="this.$bp.xs.matches ? 9 : 5"
      />
    </n-space>
  </n-space>
</template>

<script>
import {client} from "@/axios";
import {showError} from "@/utils";
import AnimeListCard from "@/components/anime/list/AnimeListCard";
import {useNotification} from "naive-ui";

export default {
  name: "AnimeList",
  components: {
    AnimeListCard,
  },
  data() {
    return {
      n: useNotification(),
      page: parseInt(this.$route.query.page) || 1,
      animes: [],
      animeCount: 0,
      animePerPage: 12,
    };
  },
  async mounted() {
    try {
      const responses = [this.fetchAnimeList()];
      if (!this.genres) responses.push(this.$store.dispatch('fetchGenres'));
      const animeResponse = (await Promise.all(responses))[0];
      this.animes = animeResponse.data.results;
      this.animeCount = animeResponse.data.count;
    } catch (e) {
      showError(this.n, "Данные не были получены!", e);
    }
  },
  async updated() {
    this.animes = [];
    this.page = parseInt(this.$route.query.page);
    window.scrollTo(0, 0);
    try {
      this.animes = (await this.fetchAnimeList()).data.results;
    } catch (e) {
      showError(this.n, "Данные не были получены!", e);
    }
  },
  watch: {
    page(newPage) {
      this.$router.push({path: this.$route.path, query: {page: newPage}});
    },
  },
  computed: {
    genres() {
      return this.$store.state.cache.genres;
    },
    cardsKeysArray() {
      return [
        ...Array(
            this.animes.length > 0 ? this.animes.length : this.animePerPage
        ).keys(),
      ];
    },
  },
  methods: {
    fetchAnimeList() {
      return client.get("/anime/", {
        params: this.$route.query,
      });
    },
  },
};
</script>

<style scoped></style>
