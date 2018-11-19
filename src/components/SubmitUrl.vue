<template>
  <div class="zz">
    <el-form :model="ruleForm" :rules="rules" ref="ruleForm">
      <el-form-item prop="url">
        <!-- can not use :model -->
        <el-input v-model="ruleForm.url" placeholder="请输入网址" clearable></el-input>
      </el-form-item>
      <el-form-item>
          <el-button type="primary" @click="submitForm('ruleForm')">加入</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
export default {
  name: 'SubmitUrl',
  data () {
    return {
      ruleForm: {
          'url': ''
      },
      rules: {
          url: [{type: 'url', required: true, message: "请输入合法url", trigger: 'blur'}]
      }
    }
  },
  methods: {
    submitForm(formName){
      var _this = this;
      this.$refs[formName].validate((valid)=>{
        if(valid){
          _this.submit()
        }
      })
    },
    submit: function(){
      var _this = this;
      _this.axios.get('http://39.107.86.245:5000/api/insert?url=' + _this.ruleForm.url)
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
    }
  }
}
</script>
