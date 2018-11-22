<template>
  <div class="zz">
    <el-form :model="ruleForm" :rules="rules" ref="ruleForm">
      <el-form-item prop="url">
        <!-- can not use :model -->
        <el-input v-model="ruleForm.url" placeholder="paste url or search by keywords" clearable></el-input>
      </el-form-item>
      <el-form-item>
          <el-button type="primary" @click="submitForm('ruleForm')">work it out</el-button>
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
          url: [{required: true, message: "tap something here", trigger: 'blur'}]
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
      _this.axios.get('http://127.0.0.1:5000/api/insert?url=' + _this.ruleForm.url)
      .then(function (response) {
        _this.$notify({
          message: response.data.msg,
          type: response.data.type
        })
      })
    }
  }
}
</script>
