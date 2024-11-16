<template>
  <div>
    <h2>File Upload</h2>
    <input type="file" @change="handleFileUpload" multiple accept="audio/*">
    <button @click="uploadFiles">Upload</button>
    <p v-if="upload_complete">Files uploaded!</p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      files: [],
      upload_complete: false,
    };
  },
  methods: {
    handleFileUpload(event) {
      this.files = event.target.files;
    },
    async uploadFiles() {
      const formData = new FormData();
      for (let file of this.files) {
        formData.append(file.name, file);
      }
      this.upload_complete = false;
      try {
        await axios.post('http://127.0.0.1:5000/transcribe', formData);
      } catch (error) {
        console.error('Upload failed:', error);
      }
      this.upload_complete = true;
    },
  },
};
</script>