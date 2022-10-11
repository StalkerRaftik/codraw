import {client} from "@/axios";

export default {
    state() {
        return {
            genres: undefined,
        };
    },
    mutations: {
        saveGenres(state, genresResponse) {
            const genres = {};
            for (const genreObj of genresResponse.data) {
                genres[genreObj.id] = genreObj.name;
            }
            state.genres = genres;
        },
    },
    actions: {
        async fetchGenres({state, commit}) {
            if (state.genres) return;

            commit('saveGenres', await client.get("/genre/"))
        },
    },
};
