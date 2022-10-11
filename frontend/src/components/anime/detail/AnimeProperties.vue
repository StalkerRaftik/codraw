<template>
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
          <n-button text tag="a" type="info" class="date-year">
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
        {{ anime.added_episodes }} из {{ anime.episodes_count }} эп.
      </n-text>
    </AnimeDetailProperty>
    <AnimeDetailProperty style="margin-top: 32px;" property-name="Рейтинг">
      <n-rate size="large" readonly allow-half style="margin-left: 8px;" :default-value="anime.raw_rating"/>
    </AnimeDetailProperty>
    <AnimeDetailProperty property-name="Просмотров">
      <n-text>
        {{ prettyNumber(anime.raw_visits, ' ') }}
      </n-text>
    </AnimeDetailProperty>
  </n-space>
</template>

<script>
import {prettyNumber} from "@/utils";
import AnimeDetailProperty from '@/components/anime/detail/AnimeDetailProperty'

export default {
  name: "AnimeProperties",
  components: {AnimeDetailProperty},
  props: {
    anime: { type: Object, required: true },
  },
  computed: {
    genres() {
      return this.$store.state.cache.genres;
    },
  },
  methods: {
    prettyNumber,
  }
}
</script>

<style scoped>
.properties span, a {
  font-size: 16px;
}

.property-margin {
  margin-top: 2px !important;
}
</style>