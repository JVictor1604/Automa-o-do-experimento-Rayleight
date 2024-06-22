const int s0 = 9;
const int s1 = 10;
const int s2 = 13;
const int s3 = 12;
const int out = 11;
const int control = 7; 

int data=0;        

void setup() 
{
   pinMode(s0,OUTPUT);   
   pinMode(s1,OUTPUT);
   pinMode(s2,OUTPUT);
   pinMode(s3,OUTPUT);
   pinMode(out,INPUT);

   Serial.begin(9600);   
   
   digitalWrite(s0,HIGH); //Putting S0/S1 on HIGH/HIGH levels means the output frequency scalling is at 100% (recommended)
   digitalWrite(s1,HIGH); 

   
}

void loop()                  //Every 0.2s we select a photodiodes set and read its data
{

   digitalWrite(s2,LOW);
   digitalWrite(s3,HIGH);
   Serial.print("Blue:");
   data=pulseIn(out,LOW);  //here we wait until "out" go LOW, we start measuring the duration and stops when "out" is HIGH again
   Serial.print(map(data,80,11,0,100));          
   Serial.print(","); //("\t");          
   delay(20);

   digitalWrite(s2,LOW);        //S2/S3 levels define which set of photodiodes we are using LOW/LOW is for RED LOW/HIGH is for Blue and HIGH/HIGH is for green
   digitalWrite(s3,LOW);
   Serial.print("Red:"); 
   data=pulseIn(out,LOW);  //here we wait until "out" go LOW, we start measuring the duration      and stops when "out" is HIGH again
   Serial.print(map(data,60,15,0,100));        
   Serial.print(","); //("\t");          
   delay(20);
                  
   digitalWrite(s2,HIGH);
   digitalWrite(s3,HIGH);
   Serial.print("Green:");
   data=pulseIn(out,LOW);  //here we wait until "out" go LOW, we start measuring the duration and stops when "out" is HIGH again
   Serial.println(map(data,80,20,0,100));          
   //Serial.print("\t");          
   delay(20);

   //Serial.println();

   delay(200);
}
