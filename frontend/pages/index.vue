<template>
<section>
    <div class="backround">
        <div class="header">
            <div style="width: 100vw;">
                <div class="header-decor"></div>
                <!-- тут должен быть username пользователя тг -->
                <p class="username">lilexport</p>
                <p class="logo">rifts</p>
            </div>
            <div class="balance">
                <p class="balance-txt">balance:</p>
                <p class="balance">3 894 249 $rift</p>
            </div>
            <div class="quest-block-navigation">
                <div class="quest-block">
                    <p class="timer">{{ timerDisplay }}</p>
                    <div class="decor-line"></div>
                    <p class="quest-txt">Log in to the game every day to earn $RIFT</p>
                    <button v-if="btn_status == true"
                        class="start-quest" 
                        ref="startButton" 
                        @click="startFillAnimation" 
                        :disabled="isButtonDisabled">
                        {{ start_txt }}
                    </button>

                    <button v-if="btn_status == false"
                        class="start-quest-no" 
                        ref="startButton" 
                        @click="startFillAnimation" 
                        :disabled="isButtonDisabled">
                        {{ start_txt }}
                    </button>
                                    
                </div>
            </div>
            <div class="theory-navigation">
                <a class="theory-txt">How to play ?</a>
            </div>
            <div class="navbar">
                <div class="navbar-block">
                    <ul>
                        <li>
                            <div class="home-block">
                                <button v-if="!home_status" @click="selectWord('home')" class="home-btn">
                                    <img src="public/home.png">
                                    <p class="navbar-txt">home</p>
                                </button>
                                <button v-if="home_status" @click="selectWord('home')" class="home-btn-animation-active">
                                    <img src="public/home.png">
                                    <p class="navbar-txt">home</p>
                                </button>
                            </div>
                        </li>
                        <li>
                            <div class="decor-line-navbar"></div>
                        </li>
                        <li>
                            <div class="home-block">
                                <button v-if="!task_status" @click="selectWord('task')" class="home-btn">
                                    <img src="public/task.png">
                                    <p class="navbar-txt">tasks</p>
                                </button>
                                <button v-if="task_status" @click="selectWord('task')" class="home-btn-animation-active">
                                    <img src="public/task.png">
                                    <p class="navbar-txt">tasks</p>
                                </button>
                            </div>
                        </li>
                        <li>
                            <div class="decor-line-navbar"></div>
                        </li>
                        <li>
                            <div class="home-block">
                                <button v-if="!friends_status" @click="selectWord('friends')" class="home-btn">
                                    <img src="public/friends.png">
                                    <p class="navbar-txt">friends</p>
                                </button>
                                <button v-if="friends_status" @click="selectWord('friends')" class="home-btn-animation-active">
                                    <img src="public/friends.png">
                                    <p class="navbar-txt">friends</p>
                                </button>
                            </div>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
</section>  
</template>

<script>
import moment from 'moment-timezone';

export default {
  data() {
    return {
      start_txt: 'start', // Original text for the button
      home_status: false,
      task_status: false,
      friends_status: false,
      WORD_ONE: 'home',
      WORD_TWO: 'task',
      WORD_THREE: 'friends',
      timerDisplay: '00:00:00',
      timeUntil14: 0, // in seconds
      timerInterval: null,
      isButtonDisabled: false,
      btn_status: true, // Reflects the button's active state
    };
  },
  mounted() {
    this.updateTimer(); // Initial call to set the timer
    this.timerInterval = setInterval(this.updateTimer, 1000); // Update every second

    // Initialize button state on mount
    this.initializeButtonState();
  },
  beforeDestroy() {
    // Clear interval to prevent memory leaks
    if (this.timerInterval) {
      clearInterval(this.timerInterval);
    }
  },
  computed: {
    lastClickTime() {
      const storedTime = localStorage.getItem('lastClickTime');
      return storedTime ? moment(storedTime) : null;
    },
  },
  methods: {
    // Timer Methods
    updateTimer() {
      const now = moment().tz('Europe/Moscow');
      const targetTime = moment().tz('Europe/Moscow').hour(14).minute(0).second(0);

      if (now.isAfter(targetTime)) {
        targetTime.add(1, 'day');
      }

      const diff = targetTime.diff(now, 'seconds');
      if (diff !== this.timeUntil14) {
        this.timeUntil14 = diff;
        this.formatTimeRemaining(diff);
      }
    },

    formatTimeRemaining(seconds) {
      const duration = moment.duration(seconds, 'seconds');
      this.timerDisplay = `${duration.hours().toString().padStart(2, '0')}:${duration.minutes()
        .toString()
        .padStart(2, '0')}:${duration.seconds().toString().padStart(2, '0')}`;
    },

    // Word Selection Method
    selectWord(selectedWord) {
      // Disable vertical swipes (Telegram WebApp specific)
      window.Telegram.WebApp.disableVerticalSwipes();

      // Reset all statuses
      this.home_status = false;
      this.task_status = false;
      this.friends_status = false;

      // Set the status for the selected word
      if (selectedWord === this.WORD_ONE) {
        this.home_status = true;
      } else if (selectedWord === this.WORD_TWO) {
        this.task_status = true;
      } else if (selectedWord === this.WORD_THREE) {
        this.friends_status = true;
      }
    },

    // Initialize Button State on Component Mount
    initializeButtonState() {
      if (this.lastClickTime) {
        const now = moment();
        const hoursSinceLastClick = now.diff(this.lastClickTime, 'hours');
        if (hoursSinceLastClick < 24) {
          this.isButtonDisabled = true;
          this.btn_status = false; // Button is disabled
          console.log('Button is disabled on load. Hours since last click:', hoursSinceLastClick);

          // Calculate remaining time and set a timer to enable the button
          const remainingMilliseconds = moment(this.lastClickTime).add(24, 'hours').diff(now);
          setTimeout(() => {
            this.isButtonDisabled = false;
            this.btn_status = true; // Button becomes active again
            console.log('Button has been re-enabled after 24 hours.');
          }, remainingMilliseconds);
        } else {
          this.isButtonDisabled = false;
          this.btn_status = true; // Button is active
        }
      }
    },

    // Button Click Handler
    startFillAnimation() {
      const now = moment();

      if (!this.lastClickTime || now.diff(this.lastClickTime, 'hours') >= 24) {
        try {
          // Save the current click time to localStorage
          localStorage.setItem('lastClickTime', now.toISOString());
          console.log('Click time saved:', now.toISOString());

          // Update button state to disabled
          this.isButtonDisabled = true;
          this.btn_status = false; // Button becomes disabled

          // Existing button animation logic
          const startButton = this.$refs.startButton;
          this.start_txt = '';
          startButton.classList.add('start-quest-animate');
          setTimeout(() => {
            startButton.classList.add('start-quest-animate-active');
          }, 10);

          setTimeout(() => {
            this.$router.push({ name: 'quests' });
          }, 500);

          // Schedule re-enabling the button after 24 hours
          setTimeout(() => {
            this.isButtonDisabled = false;
            this.btn_status = true; // Button becomes active again
            console.log('Button has been re-enabled after 24 hours.');
          }, 24 * 60 * 60 * 1000); // 24 hours in milliseconds

        } catch (e) {
          console.error('Failed to save to localStorage:', e);
          // Optionally, inform the user or implement a fallback
        }
      } else {
        // If the button should remain disabled
        this.isButtonDisabled = true;
        this.btn_status = false; // Button is disabled
        console.log('Button disabled. Time since last click:', now.diff(this.lastClickTime, 'hours'), 'hours');
      }
    }
  },
};
</script>

<style scoped>
* {
    margin: 0px;
    padding: 0px;
}


body {
    margin: 0px;
}
.backround {
    background: rgb(245, 245, 245);
    width: 100vw;
    height: 1000px;
}


.header {
    border-radius: 0px 0px 20px 20px;
    width: 100vw;
    height: 270px;
    background: linear-gradient(217.95deg, rgb(250, 222, 112) 0%,rgb(250, 208, 98) 85.887%);
}


.header-decor {
    position: absolute;
    width: 150px;
    height: 150px;
    border-radius: 0px 412px 412px 412px;
    background: rgba(255, 255, 255, 0.2);
}

.username {
    color: rgb(255, 255, 255);
    font-family: 'Bebas Neue';
    font-size: 36px;
    font-weight: 400;
    line-height: 43px;
    letter-spacing: 0px;
    text-align: left;
    float: left;
    padding: 10px 0px 0px 20px;
}

.logo {
    color: rgb(255, 255, 255);
    font-family: 'Bebas Neue';
    font-size: 48px;
    font-weight: 400;
    line-height: 58px;
    letter-spacing: 0px;
    text-align: end;
    padding: 10px 20px 0px 0px;
}

.balance-txt {
    color: rgb(255, 255, 255);
    font-family: 'Bebas Neue';
    font-size: 36px;
    font-weight: 400;
    line-height: 43px;
    letter-spacing: 0px;
    text-align: center;
    width: 100vw;
    height: 43px;
    margin: 60px 0px 0px 0px;
}

.balance {
    color: rgb(255, 255, 255);
    font-family: 'Bebas Neue';
    font-size: 48px;
    font-weight: 400;
    line-height: 58px;
    letter-spacing: 0px;
    text-align: center;
    width: 100vw;
    height: 142px;
}

.quest-block {
    border-radius: 20px 20px 50px 50px;
    background: rgb(211, 215, 218);
    width: 366px;
    height: 353px;
    margin: 40px 0px 0px 0px;
}

.quest-block-navigation {
    display: flex;
    justify-content: center;
}

.timer {
    color: rgb(255, 255, 255);
    font-family: 'Bebas Neue';
    font-size: 48px;
    font-weight: 400;
    line-height: 58px;
    letter-spacing: 0px;
    margin: 10px 0px 0px 20px;
}

.decor-line {
    width: 315px;
    height: 3px;
    border-radius: 1098px;
    background: rgb(249, 205, 98);
    margin: 4px 0px 0px 25px;
}

.quest-txt {
    width: 202px;
    height: 58px;
    color: rgb(255, 255, 255);
    font-family: 'Bebas Neue';
    font-size: 24px;
    font-weight: 400;
    line-height: 29px;
    letter-spacing: 0px;
    text-align: left;
    margin: 10px 0px 0px 20px;
}

.start-quest {
    color: rgb(255, 255, 255);
    font-family: 'Bebas Neue';
    font-size: 48px;
    font-weight: 400;
    line-height: 58px;
    letter-spacing: 0px;
    text-align: center;
    border-radius: 23px;
    background: rgb(249, 205, 98);
    width: 366px;
    height: 85px;
    border: none;
    margin: 125px 0px 0px 0px;
}

.start-quest-no {
    color: rgb(255, 255, 255);
    font-family: 'Bebas Neue';
    font-size: 48px;
    font-weight: 400;
    line-height: 58px;
    letter-spacing: 0px;
    text-align: center;
    border-radius: 23px;
    background: rgb(128, 127, 127);
    width: 366px;
    height: 85px;
    border: none;
    margin: 125px 0px 0px 0px;
}

.theory-txt {
    color: rgb(92, 135, 230);
    font-family: 'Barlow Condensed';
    font-size: 20px;
    font-weight: 400;
    line-height: 24px;
    letter-spacing: 0px;
    text-align: center;
    width: 100vw;
    height: 24px;
}

.theory-navigation {
    display: flex;
    justify-content: center;
}

.navbar-block {
    background: rgb(249, 205, 98);
    width: 100vw;
    height: 100px;
    margin: 15px 0px 0px 0px;
    position: fixed;
    bottom: 0;
    /* Центрирование */
    left: 0;
    right: 0;
    margin: 0 auto;
    display: flex;
    justify-content: center;
    align-items: center;
}

.navbar {
    position: -webkit-sticky;
    position: sticky;
}

.home-btn {
    width: 58px;
    height: 58px;
    background: none;
    border: none;
}

.home-btn-animation-active {
    width: 58px;
    height: 58px;
    background: none;
    box-sizing: border-box;
    border: 3px solid rgb(255, 255, 255);
    border-radius: 6px;
    backdrop-filter: blur(122px);
}

.navbar-txt {
    color: rgb(255, 255, 255);
    font-family: 'Bebas Neue';
    font-size: 18px;
    font-weight: 400;
    line-height: 22px;
    letter-spacing: 0px;
    text-align: center;
}

ul li {
    float: left;
    list-style: none;
}

.decor-line-navbar {
    width: 3px;
    height: 50px;
    border-radius: 1408px;
    background: rgb(255, 255, 255);
    margin: 4px 40px 0px 40px;
}

.start-quest-animate {
  position: fixed;
  top: 50%;
  left: 50%;
  width: 100vw; /* Изначальные размеры кнопки */
  height: 100vh; /* Изначальные размеры кнопки */
  background-color: rgb(249, 205, 98); /* Цвет фона кнопки */
  transform: translate(-50%, -50%) scale(0); /* Начальное состояние анимации */
  transition: transform 0.7s ease-in-out; /* Продолжительность анимации */
  border-radius: 0; /* Убираем скругление кнопки, если оно есть */
  z-index: 2; /* Убедитесь, что кнопка будет поверх других элементов */
}

/* Класс для активации анимации */
.start-quest-animate-active {
  transform: translate(-50%, -50%) scale(100); /* Конечное состояние анимации */
}
</style>
