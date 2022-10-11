<template>
  <n-space justify="center" align="center" style="margin: 24px 0 24px 0;" vertical>
    <n-card :style="$bp.md.matches ? { width: '50vw'} : { width: '95vw' }" style="min-width: 300px;" size="small">
      <n-space v-if="!anime" style="height: 500px;" vertical>
        <n-skeleton text :repeat="2"/>
        <div style="display: flex">
          <n-skeleton class="image"/>
          <div style="flex-grow: 1; margin: 8px;">
            <n-skeleton text :repeat="10" height="30px;"/>
          </div>
        </div>
      </n-space>
      <n-space v-else vertical>
        <n-h1 style="margin: 0">
          <n-text type="primary">{{ anime.name }}</n-text>
        </n-h1>
        <n-space :vertical="!$bp.sm.matches" :wrap="false" :size="[8, $bp.md.matches ? 0 : 8]">
          <img :src="anime.image" class="image" alt=""/>
          <AnimeProperties :anime="anime" />
        </n-space>
        <n-space style="margin-top: 4px;" vertical>
          <n-text class="span-header">
            Описание:
          </n-text>
          <n-ellipsis expand-trigger="click" line-clamp="4" :tooltip="false">
            <n-text>
              {{ anime.description }}
            </n-text>
          </n-ellipsis>
        </n-space>
        <n-h2 style="margin-top: 8px;">
          <n-text>Смотреть {{ anime.name }} в хорошем качестве:</n-text>
        </n-h2>
        <n-skeleton width="100%" height="400px"/>
        <n-space style="margin-top: 16px;" :size="[0,0]" vertical>
          <n-text class="span-header">Понравилось аниме? Поставьте оценку!</n-text>
          <n-rate size="large" allow-half v-model:value="userRating" :on-update:value="setUserRate" />
        </n-space>
      </n-space>
    </n-card>
  </n-space>
</template>

<script>
import {client} from "@/axios";
import {showError} from "@/utils";
import {useNotification} from "naive-ui";
import AnimeProperties from '@/components/anime/detail/AnimeProperties';

export default {
  name: "AnimeDetail",
  components: {
    AnimeProperties,
  },
  async mounted() {
    try {
      const responses = await Promise.all([
        this.fetchAnimeData(),
        this.$store.dispatch('fetchGenres')
      ]);
      this.animeResponseData = responses[0].data;
    } catch (e) {
      showError(this.n, "Данные не были получены!", e);
    }
  },
  data() {
    return {
      n: useNotification(),
      animeResponseData: null,
      userRating: 0,
      userRatingId: false,
    }
  },
  computed: {
    genres() {
      return this.$store.state.cache.genres;
    },
    anime() {
      if (!this.animeResponseData) return;

      const dataToShow = JSON.parse(JSON.stringify(this.animeResponseData));

      dataToShow.premiere_date = dataToShow.premiere_date.split('-').reverse();
      dataToShow.raw_rating = Math.round(dataToShow.raw_rating / 2);
      dataToShow.name = dataToShow.name || dataToShow.original_name;
      console.log(dataToShow)
      return dataToShow;
    }
  },
  methods: {
    async userRateChanged(value) {
      let oldValue = this.userRating;
      try {
        this.userRating = value;

      } catch (e) {
        this.userRating = oldValue;
        showError(this.n, "Ошибка во время публикации рейтинга", e);
      }
    },
    async updateUserRate(value) {
      await client.post('/rating/', {
        value: value,
        anime: this.anime.id,
      });
    },
    async createUserRate(value) {
      return await client.post('/rating/', {
        value: value,
        anime: this.anime.id,
      });
    },
    fetchAnimeData() {
      const route = this.$route
      return client.get(`/anime/${route.params.id}`, {
        params: route.query,
      });
    },
  },
}
</script>

<style scoped>
.image {
  object-fit: cover;
  width: calc(300px * 0.8);
  height: calc(500px * 0.8);
  border: 1px solid rgb(200, 200, 200);
  border-radius: 5px;
}

.properties span, a {
  font-size: 16px;
}

.span-header {
  font-size: 18px;
}
</style>