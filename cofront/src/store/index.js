import { createStore } from 'vuex'
import global from './modules/global'

export const store = createStore({
  modules: {
    global,
  }
})