<template>
  <div class="gradient-background">
  </div>
  <div class="wrapper">
    <div class="search_pmc">
      <div class="search-title">
        <h1>Поиск по Physics.Math.Code</h1>
      </div>
      <div class="search-bar">
        <input type="text" placeholder="Искать книгу..." class="glass-effect" v-model="searchQuery" @keyup.enter="search"
               @keyup="handleTyping">
      </div>

      <div id="search-results">
        <div class="search-results" v-if="searchQuery !== ''">
          <div v-for="(result, index) in searchResults" :key="index" class="tgm_wrapper">
            <telegram_message :id="result.id" :title="result.media_name" :description="result.description"/>
          </div>
        </div>
        <div v-else class="cat_wrapper">
          <img src="../assets/meme-cat-cat-meme.gif" alt="" width="300px">
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import telegram_message from "@/components/telegram_message.vue";

export default {
  name: 'BeautifulComponent',
  data() {
    return {
      searchQuery: '',
      searchResults: [],
    };
  },
  methods: {
    async search() {
      this.searchResults = []
      try {
        const response = await fetch(`https://pmce.aboba.dev/api/search/`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json;charset=utf-8'
          },
          body: JSON.stringify({"tolerance": 0, "query": this.searchQuery})
        });
        this.searchResults = await response.json()
        console.log(this.searchResults)

      } catch (error) {
        console.error('Ошибка при выполнении поиска:', error);
      }
    },
    handleTyping() {
      clearTimeout(this.typingTimer);
      this.typingTimer = setTimeout(this.search, 200);
    },
  },
  components: {
    telegram_message
  }
};
</script>

<style scoped>
.search-title {
  text-align: center;
  margin-bottom: 20px;
}

.search-title h1 {
  color: #fff; /* Белый цвет текста */
}

.gradient-background {
  background: linear-gradient(to bottom right, #ff6ec4, #7873f5);
  height: 100vh;
  width: 100%;
  display: flex;
  position: fixed;
  z-index: -1;
}

.search_pmc {
  max-width: 90%;
  display: flex;
  align-items: center;
}

.wrapper {
  display: flex;
  justify-content: center;
  align-items: center;
  padding-top: 40px;
  width: 100%;
}

.search-bar {
  display: flex;
  justify-content: flex-start;
  background-color: rgba(255, 255, 255, 0.5);
  padding: 10px;
  border-radius: 20px;
  box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
  transition: .3s;
  max-width: 320px;
  min-width: 320px;
}

.glass-effect {
  background-color: transparent;
  border: none;
  outline: none;
  //width: 300px;
  padding: 10px;
  font-size: 18px;
}

.search_pmc {
  display: flex;
  flex-direction: column;
}

.search-results {
  min-height: 70vh;
  display: flex;
  flex-wrap: wrap;
  vertical-align: baseline;
  align-items: stretch;
  position: relative;
  width: 100%;
  justify-content: space-around;
  margin-top: 50px;

}

telegram_message {
  width: 100%;
}

.tgm_wrapper {
  margin: 10px;
}

.cat_wrapper{
  padding-top: 40px;
}
.search-results > * {
  animation: fadeInUp 0.5s ease
}
.search-results img{
  margin-top: 50px;
}

@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
</style>
