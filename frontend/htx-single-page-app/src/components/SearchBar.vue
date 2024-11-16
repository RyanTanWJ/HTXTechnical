<template>
  <div>
    <h2>Search</h2>
    <input v-model="searchQuery" placeholder="Search by file name">
    <button type="button" @click="search">Search</button>
    <h2>Results</h2>
    <ul>
      <li v-for="item in resp_items" :key="item.id">
        {{ item.audio_filename }}: {{ item.transcription }}
      </li>
    </ul>
  </div>
</template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        searchQuery: '',
        resp_items: [],
      };
    },
    methods: {
      async search() {
        try {
          const response = await axios.get(`http://127.0.0.1:5000/search?search=${this.searchQuery}`);
          this.resp_items.splice(0)
          for (const trx of response.data) {
            this.resp_items.push(trx)
          }
        } catch (error) {
          console.error('Search failed:', error);
        }
      },
    },
  };
  </script>