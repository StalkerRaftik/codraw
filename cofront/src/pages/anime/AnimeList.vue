<template>
  <n-space vertical>
    <n-space
      :style="bp.xs.matches ? { width: '95vw' } : { width: '80vw' }"
      style="margin-top: 16px; margin-bottom: 16px"
      justify="space-around"
    >
      <AnimeListCard
        v-for="(animeKey, iterKey) in cardsKeysArray"
        :key="iterKey"
        :anime="animes[animeKey]"
      />
    </n-space>
    <n-space justify="center" style="margin-bottom: 24px">
      <n-pagination
        v-model:page="page"
        :page-count="Math.ceil(animeCount / animePerPage)"
        :page-slot="this.bp.xs.matches ? 5 : 9"
      />
    </n-space>
  </n-space>
</template>

<script>
import { client } from "@/axios";
import { showError } from "@/utils";
import AnimeListCard from "@/components/AnimeListCard";
import useBreakpoints from "vue-next-breakpoints";
import { useNotification } from "naive-ui";

function saveGenres(store, response) {
  const genres = {};
  for (const genreObj of response.data) {
    genres[genreObj.id] = genreObj.name;
  }
  store.state.cache.genres = genres;
}

export default {
  name: "AnimeList",
  components: {
    AnimeListCard,
  },
  setup() {
    const bp = useBreakpoints({
      xs: 550,
      md: 1200,
      lg: [1201],
    });
    return { bp };
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
      const responses = [this.getAnimePromise()];
      if (!this.genres) responses.push(client.get("/genre/"));

      const [animeResponse, genreResponse] = await Promise.all(responses);

      if (genreResponse) saveGenres(this.$store, genreResponse);
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
      this.animes = (await this.getAnimePromise()).data.results;
    } catch (e) {
      showError(this.n, "Данные не были получены!", e);
    }
  },
  watch: {
    page(newPage) {
      this.$router.push({ path: this.$route.path, query: { page: newPage } });
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
    getAnimePromise() {
      return client.get("/anime/", {
        params: this.$route.query,
      });
    },
  },
};
</script>

<style scoped></style>
