#include <string>
#include <vector>
using namespace std;

class Character {
    public:
    Character(int hp, int bonusThreshold, int recoveryPerSecond, int bonusRecovery) : 
    maxHP(hp),
    hp(hp), 
    bonusThreshold(bonusThreshold), 
    recoveryPerSecond(recoveryPerSecond), 
    bonusRecovery(bonusRecovery) { bandageTime = 0; }
    void recover() {
        hp += recoveryPerSecond;
        bandageTime++;
        if (bandageTime >= bonusThreshold) hp += bonusRecovery;
        if (hp > maxHP) hp = maxHP;
    }
    void damage(int d) {
        hp -= d;
        bandageTime = 0;
    }
    bool isDead() { return hp <= 0; }
    int hp;
    
    private:
    int maxHP;
    int bonusThreshold;
    int recoveryPerSecond;
    int bonusRecovery;
    int bandageTime;
};

int solution(vector<int> bandage, int health, vector<vector<int>> attacks) {
    Character character(health, bandage[0], bandage[1], bandage[2]);
    int attackIdx = 0;
    for (int t = 0; t < 1001; t++) {
        if (attackIdx == attacks.size()) break;
        if (attacks[attackIdx][0] == t) {
            character.damage(attacks[attackIdx][1]);
            if (character.isDead()) return -1;
            attackIdx++;
        } else {
            character.recover();
        }
    }
    return character.hp;
}
