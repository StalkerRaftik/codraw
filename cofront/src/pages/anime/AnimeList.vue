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
import { parseResponseException } from "@/utils";
import AnimeListCard from "@/components/AnimeListCard";
import useBreakpoints from "vue-next-breakpoints";
import { useNotification } from "naive-ui";

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
      notification: useNotification(),
      page: parseInt(this.$route.query.page) || 1,
      animes: [],
      animeCount: 0,
      animePerPage: 12,
    };
  },
  async mounted() { // TODO: REFACTOR THIS SCARY COMPONENT!!!!!
    try {
      const responses = [
        client.get("/anime/", {
          params: this.$route.query,
        }),
      ];
      if (!this.$store.state.cache.genres) {
        responses.push(client.get("/genre/"));
      }
      const [animeResponse, genreResponse] = await Promise.all(responses);

      if (genreResponse) {
        const genres = {};
        for (const genreObj of genreResponse.data) {
          genres[genreObj.id] = genreObj.name;
        }
        this.$store.state.cache.genres = genres;
      }
      this.animes = animeResponse.data.results;
      this.animeCount = animeResponse.data.count;
      this.animePerPage = this.animes.length;
    } catch (e) {
      this.notification.error({
        title: "Данные не были получены!",
        content: parseResponseException(e),
        duration: 10000,
      });
    }
  },
  watch: {
    async page(newPage) {
      this.animes = [];
      const query = { page: newPage };
      let queryList = [];
      for (const entry of Object.entries(query)) {
        queryList.push(`${entry[0]}=${entry[1]}`);
      }
      history.pushState({}, null, this.$route.path + `?${queryList.join("&")}`);
      window.scrollTo(0,0);
      this.$route.query = query;
      try {
        const response = await client.get("/anime/", {
          params: this.$route.query,
        });
        this.animes = response.data.results;
      } catch (e) {
        this.notification.error({
          title: "Данные не были получены!",
          content: parseResponseException(e),
          duration: 10000,
        });
      }
    },
  },
  computed: {
    genres() {
      return this.$store.state.cache.genres;
    },
    cardsKeysArray() {
      return [...Array(this.animePerPage).keys()];
    },
  },
};
</script>

<style scoped></style>
