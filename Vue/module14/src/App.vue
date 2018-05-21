<template>
    <div class="container">
        <div class="row">
            <div class="col-xs-12 col-sm-8 col-sm-offset-2 col-md-6 col-md-offset-3">
                <h1>Animations</h1>
                <hr>
                <select v-model="alertAnimation" class="form-control">
                  <option value="fade">Fade</option>
                  <option value="slide">Slide</option>
                ></select>
                <button class="btn btn-primary"  @click="show = !show">Show alert</button>
                <br><br>
                <transition :name="alertAnimation">
                    <div class="alert alert-info" v-if="show">
                        This is some info
                    </div>
                </transition>

                <transition :name="alertAnimation" type="animation" appear>
                    <div class="alert alert-info" v-show="show">
                        This is some info
                    </div>
                </transition>

                <transition 
                  enter-class=""
                  enter-active-class="animated bounce"
                  leave-class=""
                  leave-active-class="animated shake"
                  >
                    <!-- appear animation on page reload only work with own class-->
                    <div class="alert alert-info" v-if="show">
                        This is some info
                    </div>
                </transition>
                <transition :name="alertAnimation" mode="out-in">
                    <div class="alert alert-info" v-if="show" key="info">
                        This is some info
                    </div>
                    <div class="alert alert-warning" v-else="show" key="warning">
                        This is some warning
                    </div>
                </transition>
                <hr>
                <button class="btn btn-success btn-lg" @click="load = !load">Click to show</button>
                <br><br>
                <transition>
                    <div style="width:100px; height: 100px; background-color:orange;" v-if="load"></div>
                </transition>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                show:false,
                load: true,
                alertAnimation: 'fade'
            }
        }
    }
</script>

<style>
  .fade-enter {
    opacity: 0;
  }
  .fade-enter-active {
    transition: opacity 2s;
  }
  .fade-leave {
    /* opacity: 1; */
  }
  .fade-leave-active {
    transition: opacity 3s;
    opacity: 1;
  }
  .slide-enter {
      opacity: 0;
      /* transform: translateY(20px); */
  }
  .slide-enter-active {
      animation: slide-in 1s ease-out forwards;
      transition: .5s;
  }
  .slide-leave {
  }
  .slide-leave-active {
    animation: slide-out 1s ease-out forwards;
    transition: opacity 3s;
    opacity: 0;


  }
  @keyframes slide-in {
      from {
        transform: translateY(20px);
      } to {
        transform: translateY(0px);
      }
  }
  @keyframes slide-out {
      from {
        transform: translateY(0px);
      } to {
        transform: translateY(20px);
      }
  }
</style>
