<template>
  <div id="app">
    <h1>HTX Technical Frontend</h1>
    <nav>
      <RouterLink to="/">Home</RouterLink>
      <RouterLink to="/upload">Upload</RouterLink>
      <RouterLink to="/search">Search</RouterLink>
    </nav>
  </div>
  <RouterView />
</template>

<script>
import { RouterLink, RouterView } from "vue-router";
import FileUpload from "./components/FileUpload.vue";
import TranscriptionList from "./components/TranscriptionList.vue";
import SearchBar from "./components/SearchBar.vue";
import axios from "axios";

export default {
  name: "App",
  components: {
    FileUpload,
    TranscriptionList,
    SearchBar,
  },
  data() {
    return {
      transcriptions: [],
    };
  },
  methods: {
    async refreshTranscriptions() {
      try {
        const response = await axios.get("http://127.0.0.1:5000/transcriptions");
        this.transcriptions = response.data;
      } catch (error) {
        console.error("Failed to refresh transcriptions:", error);
      }
    },
    updateTranscriptions(results) {
      this.transcriptions = results;
    },
  },
  mounted() {
    this.refreshTranscriptions();
  },
};
</script>

<style>
#app {
  font-family: Arial, sans-serif;
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  display: flex;
  flex-direction: column;
}

h1 {
  text-align: center;
  color: #2c3e50;
}

header {
  text-align: center;
  font-size: 35px;
  color: white;
}

section {
  display: -webkit-flex;
  display: flex;
}
</style>
