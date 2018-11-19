<template>
  <div class="hello">
    <el-input
      placeholder="请输入网址"
      v-model="url"
      clearable>
    </el-input>
    <p></p>
    <el-button type="primary" @click="submit">提交</el-button>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      url: ''
    }
  },
  methods: {
    submit: function(){
      var _this = this;
      this.axios.get('http://localhost:5000/api/insert?url=' + this.url)
      .then(function (response) {
        if(response.data.result === true){
          _this.$notify.success({
          message: '加入成功！'
          })
        }else{
          _this.$notify.error({
          message: '加入失败！'
          })
        }
      })
    },
    // notifyResult: function(response){
    //   if(response.data.result === true){
    //     _this.$notify.success({
    //     message: '加入成功！'
    //     })
    //   }else{
    //     _this.$notify.error({
    //     message: '加入失败！'
    //     })
    //   }
    // }
  }
}
</script>
