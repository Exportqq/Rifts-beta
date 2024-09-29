<template>
    <section>
      <div class="backround-quest-two">
        <div class="navigation-sec-timer">
          <div class="sec-timer">
            {{ second_one_quest }}
          </div>
        </div>
        <div class="quset-block">
          <div class="quset-block-nav">
            <p class="quest-count-txt">{{ quest_count }}/3</p>
            <p class="quest-txt">Which of the following is a decentralized exchange (DEX) that operates on the Ethereum blockchain?</p>
          </div>
          <div class="answers-nav">
            <button 
              class="answers" 
              :class="{ 'selected': selectedAnswer === 'PoW' }" 
              @click="selectAnswer('PoW')">
              Uniswap
            </button>
            <button 
              class="answers" 
              :class="{ 'selected': selectedAnswer === 'PoS' }" 
              @click="selectAnswer('PoS')">
              Coinbase
            </button>
            <button 
              class="answers" 
              :class="{ 'selected': selectedAnswer === 'DPoS' }" 
              @click="selectAnswer('DPoS')">
              Binance
            </button>
            <button 
              class="answers" 
              :class="{ 'selected': selectedAnswer === 'BFT' }" 
              @click="selectAnswer('BFT')">
              Kraken
            </button>
  
            <button class="choose-answer" @click="submitAnswer">
              choose
            </button>
          </div>            
        </div>
      </div>
    </section>  
  </template>
      
  <script>
  export default {
    data() {
      return {
        second_one_quest: parseInt(localStorage.getItem('timerSeconds')) || 20, // Получаем значение из localStorage или устанавливаем 20
        quest_count: 2,
        selectedAnswer: null, // Состояние для отслеживания выбранного ответа
        timerInterval: null, // Переменная для хранения интервала таймера
      };
    },
    mounted() {
      this.startTimer(); // Запускаем таймер при монтировании компонента
    },
    beforeDestroy() {
      this.stopTimer(); // Останавливаем таймер перед уничтожением компонента
    },
    methods: {
      selectAnswer(answer) {
        this.selectedAnswer = answer; // Устанавливаем выбранный ответ
      },
      startTimer() {
        this.timerInterval = setInterval(() => {
          if (this.second_one_quest > 0) {
            this.second_one_quest--;
            localStorage.setItem('timerSeconds', this.second_one_quest); // Сохраняем значение в localStorage
          } else {
            this.stopTimer();
            this.redirectToNextQuest(); // Перенаправляем на следующий вопрос
          }
        }, 1000);
      },
      stopTimer() {
        clearInterval(this.timerInterval); // Останавливаем интервал
      },
      submitAnswer() {
        if (this.selectedAnswer) {
          // Здесь можно добавить логику для обработки ответа
          console.log('Selected answer:', this.selectedAnswer);
        } else {
          alert('Please select an answer');
        }
      },
      redirectToNextQuest() {
        this.$router.push({ name: 'quest_three' }); // Перенаправляем на следующий вопрос
      }
    }
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
      background: linear-gradient(111.58deg, rgb(249, 205, 98) 10.034%,rgb(209, 165, 48) 67.681%);
      width: 100vw;
      height: 1000px;
  }
  
  .backround-quest-two {
      background: linear-gradient(111.58deg, rgb(117, 203, 103) 10.034%,rgb(82, 149, 68) 67.681%);
      width: 100vw;
      height: 1000px;
  }
  
  .backround-quest-three {
      background: linear-gradient(111.58deg, rgb(214, 54, 54) 10.034%,rgb(123, 31, 31) 68.575%);
      width: 100vw;
      height: 1000px;
  }
  
  .sec-timer {
    border-radius: 354px 412px 412px 412px;
    width: 150px;
    height: 150px;
    background: rgba(255, 255, 255, 0.36);
    display: flex;
    justify-content: center;
    align-items: center;
    color: rgb(255, 255, 255);
    font-family:'Bebas Neue';
    font-size: 96px;
    font-weight: 400;
    line-height: 115px;
    letter-spacing: 0px;
    text-align: center;
  }
  
  .navigation-sec-timer {
    height: 240px;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  
  .quset-block {
    border-radius: 20px 20px 0px 0px;
    width: 100vw;
    height: 1000px;
    background: rgb(245, 245, 245);
    padding: 15px 0px 0px 0px;
  }
      
  .quest-count-txt {
    color: rgb(0, 0, 0);
    font-family: 'Bebas Neue';
    font-size: 18px;
    font-weight: 400;
    line-height: 22px;
    letter-spacing: 0px;
    width: 90vw;
    text-align: start;
  }    
  
  
  .quest-txt {
    color: rgb(0, 0, 0);
    font-family: 'Bebas Neue';
    font-size: 18px;
    font-weight: 400;
    line-height: 22px;
    letter-spacing: 0px;
    width: 90vw;
    margin: 30px 0px 10px 0px;
  }
  
  .answers { 
    box-sizing: border-box;
    border: 1px solid rgb(211, 215, 218);
    border-radius: 14px;
    width: 95vw;
    height: 56px;
    background: rgb(255, 255, 255);
    color: rgb(0, 0, 0);
    font-family: 'Bebas Neue';
    font-size: 24px;
    font-weight: 400;
    line-height: 29px;
    letter-spacing: 0px;
    text-align: center;
    margin: 10px 0px 0px 0px;
  }
  
  .answers.selected {
    border: 4px solid rgb(249, 205, 98); 
  }
  
  .choose-answer {
    box-sizing: border-box;
    border-radius: 14px;
    width: 95vw;
    height: 56px;
    border: none;
    border-radius: 14px;
    background: rgb(249, 205, 98);
    color: rgb(255, 255, 255);
    font-family: 'Bebas Neue';
    font-size: 24px;
    font-weight: 400;
    line-height: 29px;
    letter-spacing: 0px;
    text-align: center;
    margin: 10px 0px 0px 0px;
  }
  
  .answers-nav {
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  
  .quset-block-nav {
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  
  .prize-txt {
    color: rgb(123, 158, 233);
    font-family: 'Bebas Neue';
    font-size: 14px;
    font-weight: 400;
    line-height: 17px;
    letter-spacing: 0px;
    text-align: center;
    height: 25px;
    width: 90vw;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  </style>
      