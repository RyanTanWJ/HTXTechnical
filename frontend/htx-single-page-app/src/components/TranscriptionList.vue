<template>
  <div>
    <h2>Transcriptions</h2>
    <ul>
      <li v-for="transcription in transcriptions" :key="transcription.id">
        {{ transcription.audio_filename }}: {{ transcription.transcription }}
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      transcriptions: [],
    };
  },
  async mounted() {
    try {
      const response = await axios.get('http://127.0.0.1:5000/transcriptions');
      this.transcriptions.splice(0)
      for (const trx of response.data) {
        this.transcriptions.push(trx)
      }
    } catch (error) {
      console.error('Failed to fetch transcriptions:', error);
    }
  },
};
</script>