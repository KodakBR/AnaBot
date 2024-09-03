struct Rele {
  int pino;
  bool estado;
};

Rele reles[4];  // Suporta até 4 relés
int numero_reles = 4;  // Atualize conforme necessário

void setup() {
  Serial.begin(9600);

  // Configuração dos relés (deve corresponder ao arquivo INI)
  reles[0].pino = 8;  // Relé 1 (pino 8)
  reles[0].estado = false;
  pinMode(reles[0].pino, OUTPUT);
  digitalWrite(reles[0].pino, LOW);

  reles[1].pino = 9;  // Relé 2 (pino 9)
  reles[1].estado = false;
  pinMode(reles[1].pino, OUTPUT);
  digitalWrite(reles[1].pino, LOW);

  reles[2].pino = 10;  // Relé 3 (pino 10)
  reles[2].estado = false;
  pinMode(reles[2].pino, OUTPUT);
  digitalWrite(reles[2].pino, LOW);

  reles[3].pino = 11;  // Relé 4 (pino 11)
  reles[3].estado = false;
  pinMode(reles[3].pino, OUTPUT);
  digitalWrite(reles[3].pino, LOW);
}

void loop() {
  if (Serial.available() > 0) {
    String comando = Serial.readStringUntil('\n');
    comando.trim();

    for (int i = 0; i < numero_reles; i++) {
      if (comando == String("toggle ") + i) {
        reles[i].estado = !reles[i].estado;
        digitalWrite(reles[i].pino, reles[i].estado ? HIGH : LOW);
        Serial.println(reles[i].estado ? "ligado" : "desligado");
      }
    }
  }
}
