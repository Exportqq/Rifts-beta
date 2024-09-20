<template>
  <section>
    <div v-if="currentQuestion === 1" class="backround">
      <!-- Содержимое первого вопроса -->
      <div class="navigation-sec-timer">
        <div class="sec-timer">
          {{ second_one_quest }}
        </div>
      </div>
        <div class="quset-block">
          <div class="quset-block-nav">
            <p class="quest-count-txt">{{ quest_count }}/3</p>
            <p class="quest-txt">Which of the following technologies is used to ensure security and decentralization in the Bitcoin blockchain?</p>
          </div>
          <div class="answers-nav">
            <button 
              class="answers" 
              :class="{ 'selected': selectedAnswer === 'PoW' }" 
              @click="selectAnswer('PoW')">
              Proof of Work (PoW)
            </button>
            <button 
              class="answers" 
              :class="{ 'selected': selectedAnswer === 'PoS' }" 
              @click="selectAnswer('PoS')">
              Proof of Stake (PoS)
            </button>
            <button 
              class="answers" 
              :class="{ 'selected': selectedAnswer === 'DPoS' }" 
              @click="selectAnswer('DPoS')">
              Delegated Proof of Stake (DPoS)
            </button>
            <button 
              class="answers" 
              :class="{ 'selected': selectedAnswer === 'BFT' }" 
              @click="selectAnswer('BFT')">
              Byzantine Fault Tolerance (BFT)
            </button>
  
            <button class="choose-answer" @click="handleChoose">
              choose
            </button>
            <p class="prize-txt">50-100 $RIFTS</p>
          </div>
      </div>
    </div>

    <div v-else-if="currentQuestion === 2" class="backround-quest-two">
      <!-- Содержимое второго вопроса -->
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
            :class="{ 'selected': selectedAnswer === 'Uniswap' }" 
            @click="selectAnswer('Uniswap')">
            Uniswap
          </button>
          <button 
            class="answers" 
            :class="{ 'selected': selectedAnswer === 'Coinbase' }" 
            @click="selectAnswer('Coinbase')">
            Coinbase
          </button>
          <button 
            class="answers" 
            :class="{ 'selected': selectedAnswer === 'Binance' }" 
            @click="selectAnswer('Binance')">
            Binance
          </button>
          <button 
            class="answers" 
            :class="{ 'selected': selectedAnswer === 'Kraken' }" 
            @click="selectAnswer('Kraken')">
            Kraken
          </button>

          <button class="choose-answer" @click="handleChoose">
              choose
          </button>
          <p class="prize-txt">50-100 $RIFTS</p>
          <p>{{ prize }}</p>
        </div> 
      </div>
    </div>




    <div v-else-if="currentQuestion === 3" class="backround-quest-three">
      <!-- Содержимое третьего вопроса -->
      <div class="navigation-sec-timer">
        <div class="sec-timer">
          {{ second_one_quest }}
        </div>
      </div>
      <div class="quset-block">
        <div class="quset-block-nav">
          <p class="quest-count-txt">{{ quest_count }}/3</p>
          <p class="quest-txt">Which technology underlies Bitcoin, ensuring the immutability and transparency of transactions?</p>
        </div>
        <div class="answers-nav">
          <button 
            class="answers" 
            :class="{ 'selected': selectedAnswer === 'Blockchain' }" 
            @click="selectAnswer('Blockchain')">
            Blockchain
          </button>
          <button 
            class="answers" 
            :class="{ 'selected': selectedAnswer === 'AI' }" 
            @click="selectAnswer('AI')">
            Artificial Intelligence (AI)
          </button>
          <button 
            class="answers" 
            :class="{ 'selected': selectedAnswer === 'Cloud' }" 
            @click="selectAnswer('Cloud')">
            Cloud Computing
          </button>
          <button 
            class="answers" 
            :class="{ 'selected': selectedAnswer === 'Quantum' }" 
            @click="selectAnswer('Quantum')">
            Quantum Computing
          </button>

          <button class="choose-answer" @click="handleChoose">
            choose
          </button>
          <p class="prize-txt">50-100 $RIFTS</p>
          <p>Total prize: {{ prize }} $RIFTS</p>
        </div> 
      </div>
    </div>




    <div v-else-if="currentQuestion === 4" class="backround-quest-three">

          <p>Total prize: {{ prize }} $RIFTS</p>
          <button @click="navigateToHome">back home</button>
    </div>

    
  </section>  
</template>


<script>
export default {
  data() {
    return {
      prize: 0,
      second_one_quest: parseInt(localStorage.getItem('timerSeconds')) || 20,
      quest_count: 1,
      selectedAnswer: null,
      timerInterval: null,
      currentQuestion: 1,
    };
  },
  mounted() {
    this.startTimer();
  },
  beforeDestroy() {
    this.stopTimer();
  },
  methods: {
    selectAnswer(answer) {
      this.selectedAnswer = answer;
    },
    navigateToHome() {
      this.$router.push({ name: 'index' });
    },
    handleChoose() {
      if (this.selectedAnswer) {
        let correctAnswer;
        switch(this.currentQuestion) {
          case 1:
            correctAnswer = 'PoW';
            break;
          case 2:
            correctAnswer = 'Uniswap';
            break;
          case 3:
            correctAnswer = 'Blockchain';
            break;
        }
        
        if (this.selectedAnswer === correctAnswer) {
          const reward = Math.floor(Math.random() * (100 - 50 + 1)) + 50;
          this.prize += reward;
          console.log(`Correct answer! You won ${reward} $RIFTS. Total prize: ${this.prize} $RIFTS`);
        } else {
          console.log(`Incorrect answer. No $RIFTS awarded. Total prize: ${this.prize} $RIFTS`);
        }
        
        this.stopTimer();
        this.moveToNextQuestion();
      } else {
        alert('Please select an answer');
      }
    },
    startTimer() {
      this.timerInterval = setInterval(() => {
        if (this.second_one_quest > 0) {
          this.second_one_quest--;
          localStorage.setItem('timerSeconds', this.second_one_quest);
        } else {
          this.stopTimer();
          this.moveToNextQuestion();
        }
      }, 1000);
    },
    stopTimer() {
      clearInterval(this.timerInterval);
    },
    moveToNextQuestion() {
      this.currentQuestion++;
      this.selectedAnswer = null;
      this.second_one_quest = 20;
      this.quest_count++;
      localStorage.setItem('timerSeconds', this.second_one_quest);
      if (this.currentQuestion > 3) {
        // Если все вопросы закончились, можно перенаправить на страницу результатов
        console.log('Quiz completed! Total prize:', this.prize);
        // this.$router.push({ name: 'results', params: { prize: this.prize } });
      } else {
        this.startTimer();
      }
    },
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
    