<template>
    <div class="flex flex-col bg-white shadow-2xl p-10 rounded-3xl w-2/3">
        <h1 class="text-2xl font-bold mb-5">{{ title }}</h1>
        <p>{{ text }}</p>
        <img class="object-cover w-full h-52 rounded-2xl mt-5" :src="image" alt="">
        <div class="flex mt-5 flex-wrap">
            <div v-for="keyword in keywords.slice(-7)">
                <div class="border border-purple-700 p-2 rounded-full mr-2">
                    {{ keyword }}
                </div>
            </div>
        </div>
        <a v-if="link != 'false'" :href="link"
            class="text-center transition-all mt-5 text-gray-400 hover:bg-purple-200 rounded-2xl py-3 hover:border-purple-700 border-2 hover:text-purple-700">Читать
            далее...</a>
    </div>
</template>

<script>
export default {
    props: ['image', 'title', 'text', 'link', 'keywords'],
}
</script>