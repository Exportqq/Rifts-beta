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
                    <p class="timer">23:24:09</p>
                    <div class="decor-line"></div>
                    <p class="quest-txt">Log in to the game every day to earn $RIFT</p>
                    <button class="start-quest">start</button>
                </div>
            </div>
            <div class="theory-navigation">
                <a class="theory-txt">How to play ?</a>
            </div>
            <div class="navbar">
                <div class="navbar-block">

                </div>
            </div>
        </div>
    </div>
</section>  
</template>

<script>
export default {
  data() {
    return {
      WORD_ONE: 'Bitcoin',
      WORD_TWO: 'Ethereum',
      WORD_THREE: 'Solana',
      WORD_FOUR: 'Cardano',
      WORD_ONE_status: false,
      WORD_TWO_status: false,
      WORD_THREE_status: false,
      WORD_FOUR_status: false,
    }},
    methods: {
        selectWord(selectedWord) {
            // Сброс всех статусов
            this.WORD_ONE_status = false;
            this.WORD_TWO_status = false;
            this.WORD_THREE_status = false;
            this.WORD_FOUR_status = false;

            // Установка статуса для выбранного слова
            if (selectedWord === 'WORD_ONE') {
                this.WORD_ONE_status = true;
            } else if (selectedWord === 'WORD_TWO') {
                this.WORD_TWO_status = true;
            } else if (selectedWord === 'WORD_THREE') {
                this.WORD_THREE_status = true;
            } else if (selectedWord === 'WORD_FOUR') {
                this.WORD_FOUR_status = true;
            }
        }
    }
  }
    
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
    height: 800px;
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
}

.navbar {
    position: fixed;
}
</style>
