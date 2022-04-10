<template>
  <n-space justify="center" align="center" style="margin: 24px 0 24px 0;" vertical>
    <n-card :style="bp.md.matches ? { width: '50vw'} : { width: '95vw' }" style="min-width: 300px;" size="small">
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
        <n-space :vertical="!bp.sm.matches" :wrap="false" :size="[8, bp.md.matches ? 0 : 8]">
          <img :src="anime.image" class="image" alt=""/>
          <n-space class="properties" vertical :size="[0, 0]">
            <AnimeDetailProperty property-name="Год выпуска">
              <n-space :size="[0,0]">
                <n-text>
                  {{ anime.premiere_date[0] }}.
                </n-text>
                <n-text>
                  {{ anime.premiere_date[1] }}.
                </n-text>
                <router-link
                    :to="{ name: 'AnimeList', query: { year: anime.premiere_date[2] }}"
                >
                  <n-button text tag="a" type="info">
                    {{ anime.premiere_date[2] }}
                  </n-button>
                </router-link>
              </n-space>
            </AnimeDetailProperty>
            <AnimeDetailProperty class="property-margin" property-name="Жанры">
              <div v-for="(genreId, arrKey) in anime.genres" :key="genreId" style="display: flex;">
                <router-link
                    :to="{ name: 'AnimeList', query: { genre: genreId }}"
                >
                  <n-button text tag="a" type="info">
                    {{ genres[genreId] }}
                  </n-button>
                </router-link>
                <span style="margin-right: 4px">
                    {{ arrKey !== anime.genres.length - 1 ? ',' : '' }}
                  </span>
              </div>
            </AnimeDetailProperty>
            <AnimeDetailProperty class="property-margin" property-name="Статус">
              <router-link
                  :to="{ name: 'AnimeList', query: { status: anime.status }}"
              >
                <n-button text tag="a" type="info">
                  {{ $t(anime.status) }}
                </n-button>
              </router-link>
            </AnimeDetailProperty>
            <AnimeDetailProperty class="property-margin" property-name="Серии">
              <n-text>
                1-{{ anime.added_episodes }} из {{ anime.episodes_count }} эп.
              </n-text>
            </AnimeDetailProperty>
            <AnimeDetailProperty style="margin-top: 16px;" property-name="Рейтинг">
              <n-rate size="large" readonly allow-half style="margin-left: 8px;" :default-value="anime.raw_rating"/>
            </AnimeDetailProperty>
            <AnimeDetailProperty property-name="Просмотров">
              <n-text>
                {{ prettyNumber(anime.raw_visits, ' ') }}
              </n-text>
            </AnimeDetailProperty>
          </n-space>
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
          <n-rate size="large" allow-half :default-value="0"/>
        </n-space>
      </n-space>
    </n-card>
  </n-space>
</template>

<script>
import bp from "@/breakpoints";
import {client} from "@/axios";
import {showError, prettyNumber} from "@/utils";
import {useNotification} from "naive-ui";
import AnimeDetailProperty from '@/components/AnimeDetailProperty'
import $t from '@/i18n'

export default {
  name: "AnimeDetail",
  components: {
    AnimeDetailProperty,
  },
  async mounted() {
    try {
      const responses = [this.getAnimePromise()];
      if (!this.genres) responses.push(this.$store.dispatch('fetchGenres'));
      const animeResponse = (await Promise.all(responses))[0];
      this.animeResponseData = animeResponse.data;
    } catch (e) {
      showError(this.n, "Данные не были получены!", e);
    }
  },
  data() {
    return {
      bp,
      n: useNotification(),
      animeResponseData: null,
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
    $t,
    prettyNumber,
    getAnimePromise() {
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

.property-margin {
  margin-top: 2px !important;
}

.span-header {
  font-size: 18px;
}
</style>