<template>
  <div class="card" :class="{ 'open': isOpen }">
    <div class="header">
      <div class="file_icon" @click="toTg(id)">
        <div class="background"></div>
        <svg height='30' viewBox='0 0 30 30' width='30' xmlns='http://www.w3.org/2000/svg'>
          <path
              d='m16.6538365 4.06433079c.1979918.04563221.3731812.11819804.5454493.22593253l.1128317.07532436c.1136531.08153308.2382757.18981438.4504173.39794253l5.3612119 5.36021649c.3651614.3651614.4782555.5046993.58599.6769675.1077345.1722681.1803003.3474575.2259325.5454493l.0265217.1330464c.0264976.1610204.0378091.3583423.0378091.7599994v11.1969055c0 .8915187-.0928256 1.214805-.2671327 1.5407309s-.4300957.5817145-.7560216.7560216-.6492122.2671327-1.5407309.2671327h-12.8722296c-.89151874 0-1.21480498-.0928256-1.5407309-.2671327-.32592593-.1743071-.5817145-.4300957-.7560216-.7560216-.16089885-.3008547-.2523697-.5994602-.26549007-1.3448229l-.00164263-17.0681376c0-.89151874.09282561-1.21480498.2671327-1.5407309.1743071-.32592593.43009567-.5817145.7560216-.7560216.3008547-.16089885.5994602-.2523697 1.34482293-.26549007l7.39281347-.00164263c.5164163 0 .695054.01869859.8930458.06433079zm-.5073899 2.7892226c-.0937682.09376819-.1464466.22094515-.1464466.35355339v3.79289322c0 .5522847.4477153 1 1 1h3.7928932c.2761424 0 .5-.2238576.5-.5 0-.1326082-.0526784-.2597852-.1464466-.3535534l-4.2928932-4.29289321c-.1952622-.19526215-.5118446-.19526215-.7071068 0z'
              fill='#cccccc' fill-rule='evenodd'/>
        </svg>
      </div>
      <span class="title">{{ title }}</span>
      <span v-if="description">
        <span v-if="isOpen" class="arrow" @click="toggleDescription">&#8964;</span>
        <span v-else class="arrow" @click="toggleDescription">&#8963;</span>
      </span>
    </div>
    <div v-if="isOpen" class="description">
      <span>{{ description }}</span>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      isOpen: false,
    };
  },
  props: {
    title: {
      type: String,
      required: true
    },
    description: {
      type: String,
      required: false
    },
    id: {
      type: Number,
      required: true
    }
  },
  methods: {
    toggleDescription() {
      if (this.description !== "") {
        this.isOpen = !this.isOpen;
      }
    },
    toTg(id) {
      window.open("https://t.me/physics_lib/" + id)
    }
  }
};
</script>

<style scoped>
.card {
  min-height: 60px;
  border-radius: 10px;
  overflow: hidden;
  margin-bottom: 20px;
  max-width: 320px;
  min-width: 320px;
  color: #dcdcdc;
  height: 100%;
  margin-top: 5px;
  margin-left: 5px;
  margin-right: 5px;
}

.card:hover {
  cursor: default;
}

.header {
  background-color: #1c1c1c;
  border: 1px solid #ccc;
  padding: 17px 10px;
  cursor: pointer;
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 100%;
  max-height: 100px;
}

.title {
  color: #dcdcdc;
  font-weight: bold;
  text-align: start;
  width: 100%;
  margin-left: 15px;
  text-overflow: ellipsis;
  overflow: hidden;
  max-width: 200px;
  font-size: 15px;
}

.arrow {
  font-size: 1.2em;
}

.description {
  color: #333333;
  background-color: #cccccc;
  min-height: 100px;
  border: 1px solid #ccc;
  border-radius: 0 0 10px 10px;
  padding: 5px;
}

.description span {
  display: flex;
  justify-content: center;
  width: 100%;
}

.file_icon {
  position: relative;
  padding-left: 10px;
  width: 50px;
  height: 50px;
}

.background {
  background-color: #4ca3e2;
  height: 45px;
  display: block;
  width: 45px;
  border-radius: 50%;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  animation: pulse 2s ease-in-out infinite;
}

@keyframes pulse {
  0% {

  }
  50% {
    box-shadow: #cccccc 0 0 3px 2px;
  }
}

svg {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  fill: #cccccc;
}
</style>
