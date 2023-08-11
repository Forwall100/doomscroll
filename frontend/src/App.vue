<script>
import TheCard from './components/TheCard.vue';
import axios from 'axios'

export default {
  components: {
    TheCard
  },
  data() {
    return {
      image: '',
      title: '',
      link: false,
      text: null,
      keywords: [],
      loading: false,
      errorMessage: "",
      sourceName: "",
      categories: [],
      selected_category: "Все"
    }
  },
  methods: {
    async get_post() {
      this.loading = true
      try {
        let data
        console.log('start')
        if (this.selected_category == "Все") {
          await axios
            .get("http://127.0.0.1:8000/post")
            .then(responce => (data = responce.data))
        } else {
          await axios
            .get("http://127.0.0.1:8000/post-by-category?category=" + this.selected_category)
            .then(responce => (data = responce.data))
        }
        this.image = data['image']
        this.title = data['title']
        this.text = data['summary']
        this.link = data['link']
        this.keywords = data['keywords']
        this.sourceName = data['source_title']
        this.errorMessage = ''
      } catch (err) {
        this.loading = false
        console.log('ERRROR:' + err)
      }

      this.loading = false
    },
    async get_categories() {
      let data
      await axios
        .get("http://127.0.0.1:8000/get-categories")
        .then(responce => (data = responce.data))
      this.categories = data['categories']
    },
  },
  mounted() {
    this.get_post()
    this.get_categories()
  }

}
</script>

<template>
  <div class="flex justify-center mt-10 px-28">
    <div class="felx-col">
      <div class="flex gap-5">
        <img src="./assets/logo.svg" class="h-8 w-8" alt="">
        <h1 class="mb-10 font-bold text-xl">Категории:</h1>
      </div>
      <div @click="selected_category = 'Все'" class="hover:cursor-pointer mb-5 transition-all"
        :class="selected_category == 'Все' ? 'text-purple-700' : 'hover:text-purple-700'">Все</div>
      <div v-for="category in categories" @click="selected_category = category"
        class="hover:cursor-pointer mb-5 transition-all"
        :class="category == selected_category ? 'text-purple-700' : 'hover:text-purple-700'">{{ category }}</div>
    </div>
    <div class="flex justify-center w-full items-center gap-10">
      <Transition name="slide-fade" mode="out-in">
        <TheCard v-if="!loading" :image="image" :title="title" :link="link" :text="text" :keywords="keywords"
          :source="sourceName" />
        <svg v-else xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
          stroke="currentColor" class="w-6 h-6 animate-spin">
          <path stroke-linecap="round" stroke-linejoin="round"
            d="M16.023 9.348h4.992v-.001M2.985 19.644v-4.992m0 0h4.992m-4.993 0l3.181 3.183a8.25 8.25 0 0013.803-3.7M4.031 9.865a8.25 8.25 0 0113.803-3.7l3.181 3.182m0-4.991v4.99" />
        </svg>
      </Transition>
    </div>
  </div>

  <div class="fixed z-50 bottom-5 right-5 mt-5">
    <button @click="get_post"
      class="bg-purple-600 text-white hover:text-purple-700 flex hover:bg-purple-100 hover:ring-2 hover:ring-purple-500 px-5 py-3 rounded-2xl transition-all">
      Далее
      <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor"
        class="w-6 h-6 ml-5">
        <path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12h15m0 0l-6.75-6.75M19.5 12l-6.75 6.75" />
      </svg>
    </button>
  </div>
</template>

<style>
.slide-fade-enter-active {
  transition: all 0.3s ease-out;
}

.slide-fade-leave-active {
  transition: all 0.3s cubic-bezier(1, 0.5, 0.8, 1);
}

.slide-fade-enter-from,
.slide-fade-leave-to {
  transform: translateY(-20px);
  opacity: 0;
}
</style>