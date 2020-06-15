<template>
  <view class="container">
    <text class="text-color-primary">Image Processing</text>
    <button v-bind:title="message" v-bind:on-press="handleBtnPress" />

    <!-- <template> -->
    <view class="parent-container">
      <view class="container">
        <animatedView
          class="animated-view-style"
          :style="{
          marginBottom: movingMargin,
          backgroundColor: 'red',
        }"
        />
        <animatedView
          class="animated-view-style"
          :style="{
          marginBottom: movingMargin1,
          backgroundColor: 'green',
        }"
        />
        <animatedView
          class="animated-view-style"
          :style="{
          marginBottom: movingMargin2,
          backgroundColor: 'blue',
        }"
        />
        <animatedView
          class="animated-view-style"
          :style="{
          marginBottom: movingMargin3,
          backgroundColor: 'purple',
        }"
        />
      </view>
    </view>
    <!-- </template> -->
  </view>
  <!-- // </template> -->
  <!-- </view> -->
</template>


<script>
export default {
  data: function() {
    return {
      message: "Hello Aurio Pinto"
    };
  },
  methods: {
    handleBtnPress: function() {
      alert("Image Visualization");
    },
    animate: function() {
      this.animatedValue.setValue(0);
      this.animatedValue1.setValue(0);
      this.animatedValue2.setValue(0);
      this.animatedValue3.setValue(0);

      animated
        .stagger(100, [
          animated.timing(this.animatedValue3, {
            toValue: 2,
            duration: this.duration,
            easing: Easing.linear
          }),

          animated.timing(this.animatedValue2, {
            toValue: 2,
            duration: this.duration,
            easing: Easing.linear
          }),

          animated.timing(this.animatedValue1, {
            toValue: 2,
            duration: this.duration,
            easing: Easing.linear
          }),
          animated.timing(this.animatedValue, {
            toValue: 2,
            duration: this.duration,
            easing: Easing.linear
          })
        ])
        .start(event => {
          if (event.finished) {
            this.animate();
          }
        });
      this.movingMargin = this.animatedValue.interpolate({
        inputRange: [0, 0.5, 1, 1.5, 2],
        outputRange: [0, 200, 0, 200, 0]
      });
      this.movingMargin1 = this.animatedValue1.interpolate({
        inputRange: [0, 0.5, 1, 1.5, 2],
        outputRange: [0, 200, 0, 200, 0]
      });
      this.movingMargin2 = this.animatedValue2.interpolate({
        inputRange: [0, 0.5, 1, 1.5, 2],
        outputRange: [0, 200, 0, 200, 0]
      });
      this.movingMargin3 = this.animatedValue3.interpolate({
        inputRange: [0, 0.5, 1, 1.5, 2],
        outputRange: [0, 200, 0, 200, 0]
      });
    }
  }
};
</script>

<style>
.container {
  background-color: white;
  align-items: center;
  justify-content: center;
  flex: 1;
}
.text-color-primary {
  color: blue;
}

.animated-view-style {
  height: 50;
  width: 50;
  border-radius: 50;
}
.container {
  flex-direction: "row";
  justify-content: "space-evenly";
  align-items: "flex-end";
  height: 300;
}
.parent-container {
  flex-direction: "column";
  justify-content: "center";
}
</style>
