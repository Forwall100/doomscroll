<template>
    <div v-if="!loading" class="flex flex-col bg-white shadow-2xl p-10 rounded-3xl w-2/3">
        <h1 class="text-2xl font-bold mb-5">{{ title }}</h1>
        <p v-if="!isgpt">{{ text }}</p>
        <p v-else>{{ summary }}</p>
        <img class="object-cover w-full h-52 rounded-2xl mt-5" :src="image" alt="">
        <div class="flex mt-5 flex-wrap">
            <div v-for="keyword in keywords.slice(-7)">
                <div class="border border-purple-700 p-2 rounded-full mb-2 mr-2">
                    {{ keyword }}
                </div>
            </div>
        </div>
        <div class="flex w-full items-center gap-5">
            <button
                class="flex w-full justify-center text-center transition-all mt-5 px-5 text-gray-400 hover:bg-purple-200 rounded-2xl py-3 hover:border-purple-700 border-2 hover:text-purple-700">
                <a v-if="link != 'false'" :href="link">Читать
                    далее...</a>
            </button>
            <button @click="gptize"
                class="flex w-full justify-center text-center transition-all mt-5 px-5 text-gray-400 hover:bg-purple-200 rounded-2xl py-3 hover:border-purple-700 border-2 hover:text-purple-700">
                <svg class="h-7 w-7 mr-2" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                    <path
                        d="M22.2819 9.8211a5.9847 5.9847 0 0 0-.5157-4.9108 6.0462 6.0462 0 0 0-6.5098-2.9A6.0651 6.0651 0 0 0 4.9807 4.1818a5.9847 5.9847 0 0 0-3.9977 2.9 6.0462 6.0462 0 0 0 .7427 7.0966 5.98 5.98 0 0 0 .511 4.9107 6.051 6.051 0 0 0 6.5146 2.9001A5.9847 5.9847 0 0 0 13.2599 24a6.0557 6.0557 0 0 0 5.7718-4.2058 5.9894 5.9894 0 0 0 3.9977-2.9001 6.0557 6.0557 0 0 0-.7475-7.0729zm-9.022 12.6081a4.4755 4.4755 0 0 1-2.8764-1.0408l.1419-.0804 4.7783-2.7582a.7948.7948 0 0 0 .3927-.6813v-6.7369l2.02 1.1686a.071.071 0 0 1 .038.052v5.5826a4.504 4.504 0 0 1-4.4945 4.4944zm-9.6607-4.1254a4.4708 4.4708 0 0 1-.5346-3.0137l.142.0852 4.783 2.7582a.7712.7712 0 0 0 .7806 0l5.8428-3.3685v2.3324a.0804.0804 0 0 1-.0332.0615L9.74 19.9502a4.4992 4.4992 0 0 1-6.1408-1.6464zM2.3408 7.8956a4.485 4.485 0 0 1 2.3655-1.9728V11.6a.7664.7664 0 0 0 .3879.6765l5.8144 3.3543-2.0201 1.1685a.0757.0757 0 0 1-.071 0l-4.8303-2.7865A4.504 4.504 0 0 1 2.3408 7.872zm16.5963 3.8558L13.1038 8.364 15.1192 7.2a.0757.0757 0 0 1 .071 0l4.8303 2.7913a4.4944 4.4944 0 0 1-.6765 8.1042v-5.6772a.79.79 0 0 0-.407-.667zm2.0107-3.0231l-.142-.0852-4.7735-2.7818a.7759.7759 0 0 0-.7854 0L9.409 9.2297V6.8974a.0662.0662 0 0 1 .0284-.0615l4.8303-2.7866a4.4992 4.4992 0 0 1 6.6802 4.66zM8.3065 12.863l-2.02-1.1638a.0804.0804 0 0 1-.038-.0567V6.0742a4.4992 4.4992 0 0 1 7.3757-3.4537l-.142.0805L8.704 5.459a.7948.7948 0 0 0-.3927.6813zm1.0976-2.3654l2.602-1.4998 2.6069 1.4998v2.9994l-2.5974 1.4997-2.6067-1.4997Z" />
                </svg>
                Скормить GPT
            </button>
        </div>
        <div class="mt-5 text-gray-400">Источник: {{ source }}</div>
    </div>
    <div class="flex" v-else>
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor"
            class="w-6 h-6 animate-spin">
            <path stroke-linecap="round" stroke-linejoin="round"
                d="M16.023 9.348h4.992v-.001M2.985 19.644v-4.992m0 0h4.992m-4.993 0l3.181 3.183a8.25 8.25 0 0013.803-3.7M4.031 9.865a8.25 8.25 0 0113.803-3.7l3.181 3.182m0-4.991v4.99" />
        </svg>
        <h1 class="ml-5">
            GPT думает...
        </h1>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    props: ['image', 'title', 'text', 'link', 'keywords', 'source'],
    data() {
        return {
            loading: false,
            errorMessage: "",
            summary: "",
            isgpt: false
        }
    },
    methods: {
        async gptize() {
            this.loading = true
            try {
                let data
                console.log('start')
                await axios
                    .get("http://127.0.0.1:8000/gptize/?article_url=" + this.link)
                    .then(responce => (data = responce.data))
                console.log('stop')
                console.log(data)
                this.summary = data['summary']
                this.isgpt = true
                this.errorMessage = ''
            } catch (err) {
                this.loading = false
                this.errorMessage = ""
            }

            this.loading = false
        }
    }
}
</script>