const int trigPin = 3;  // Mendefinisikan pin 3 sebagai trigPin
const int echoPin = 4;  // Mendefinisikan pin 4 sebagai echoPin

long duration;          // Variabel untuk menyimpan durasi sinyal
int distance;           // Variabel untuk menyimpan jarak yang diukur


void setup() {
  Serial.begin(9600);    // Init komunikasi serial dengan baud rate 9600
  pinMode(trigPin, OUTPUT); // Mengatur pin trigPin sebagai output
  pinMode(echoPin, INPUT);  // Mengatur pin echoPin sebagai input
}

void loop() {
  digitalWrite(trigPin, LOW);   // Mengatur trigPin ke level rendah
  delayMicroseconds(2);         // Memberi jeda selama 2 mikrodetik
  digitalWrite(trigPin, HIGH);  // Mengatur trigPin ke level tinggi
  delayMicroseconds(10);       // Mempertahankan level tinggi selama 10ms
  digitalWrite(trigPin, LOW);   // Mengatur trigPin ke level rendah

  duration = pulseIn(echoPin, HIGH); // Mengukur durasi sinyal tinggi
  distance = duration * 0.034 / 2;   // Menghitung jarak durasi sinyal
  Serial.print("Jarak = ");          // Mencetak teks ke Serial Monitor
  Serial.print(distance);            // Mencetak nilai jarak yang diukur
  Serial.println(" cm");             // Mencetak dan pindah ke baris baru
  delay(200);                        // Menunggu selama 200 milidetik
}
