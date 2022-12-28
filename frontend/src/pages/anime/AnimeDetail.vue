<template>
  <n-space justify="center" align="center" style="padding: 24px 0;" vertical>
    <n-card style="min-width: 300px; width: 95vw;" size="small">
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
          <n-ellipsis expand-trigger="click" line-clamp="4" :tooltip="false" style="padding-right: 64px;">
            <n-text>
              {{ anime.description }}
            </n-text>
          </n-ellipsis>
        </n-space>
        <n-h2 style="margin-top: 8px;">
          <n-text>Смотреть {{ anime.name }} в хорошем качестве:</n-text>
        </n-h2>
        <n-skeleton width="100%" height="400px"/>
        <n-space justify="center" style="margin: 24px 0;">
          <n-space style="margin-top: 16px; gap: 8px;" :size="[0,0]" vertical align="center">
            <n-text class="span-header">
              {{userRating ? `Вы оценили это аниме. Ваша оценка - ${userRating}` : "Понравилось аниме? Поставьте оценку!"}}
            </n-text>
            <n-rate size="large" allow-half v-model:value="userRating" />
          </n-space>
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
      this.userRating = this.animeResponseData.user_rating
    } catch (e) {
      showError(this.n, "Данные не были получены!", e);
    }
  },
  data() {
    return {
      n: useNotification(),
      animeResponseData: null,
      userRating: null,
    }
  },
  watch: {
    async userRating(newValue, oldValue) {
      if (!oldValue) return
      try {
        await this.updateUserRate(newValue)
        this.n.success({
          title: "Оценка обновлена",
          duration: 3000,
        });
      }
      catch (e) {
        showError(this.n, 'Оценка не обновлена', e)
      }
    },
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
    async updateUserRate(value) {
      await client.post(`/anime/${this.$route.params.id}/set_user_rating/`, {
        value: value,
      });
    },
    async fetchAnimeData() {
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