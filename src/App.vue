<template>
  <div id="app">
    <!-- <img src="./assets/logo.png"> -->
    <!-- <HelloWorld/> -->
    <SubmitUrl/>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld'
import SubmitUrl from './components/SubmitUrl'

export default {
  name: 'App',
  components: {
    HelloWorld,
    SubmitUrl
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 200px;
}
</style>
