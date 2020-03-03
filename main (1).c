#include <stdio.h>
#include <stdlib.h>
//enum oem {"Samsung","Apple","One plus","HTC"};
struct mobile{
int umn;
float displaysize;
int batterycapacity;
int ram;
int rom;
int camera;
int price};
typedef struct mobile mobile;
void display(mobile *);
int average(const mobile *,int);
int maxbattery(const mobile*,int);
int maxcamera(const mobile *,int);

int main()
{
    int n=4;
    mobile m[4]={{101,6.3,4000,6,512,12,400},{102,6,3000,8,128,16,500},{103,6.8,8000,4,128,12,900},{104,8,1000,8,16,18,700}};
    mobile *ptr= malloc(n*sizeof(mobile));
    mobile *p=m;
    for(int i = 0; i<n ; i++){
        display(p++);
    }
    average(m,n);
    int count=0;
    for(int i=0;i<n;i++){
        if(m[i].rom<32){
            count++;
        }
    }
    printf("mobile with miminum storage=%d\n",count);
    maxbattery(m,n);
    maxcamera(m,n);


    /*for(int i=0;i<n;i++){
        scanf("umn=%d,displaysize=%f inches,batterycapacity=%lf Mah,ram=%d GB,rom=%d GB,camera =%d MP price =$%lf\n",ptr->umn, ptr->displaysize,ptr->batterycapacity,ptr->ram,ptr->rom,ptr->camera,ptr->price);
        ptr++;*/
    return 0;
}
void display(mobile *ptr1){
    printf("umn=%d,displaysize=%f inches,batterycapacity=%d Mah,ram=%d Gb,rom=%d GB,camera =%d MP price =$%d\n\n\n",ptr1->umn, ptr1->displaysize,ptr1->batterycapacity,ptr1->ram,ptr1->rom,ptr1->camera,ptr1->price);
}
int average(const mobile *ptr2,int l){
    int sum = 0;
    const mobile *parr=ptr2;
    for(int i = 0; i<l ; i++){
    sum+=parr->price;
    parr++;
    }
    printf("avgerage price of phone =$%d\n",sum/l);

}
int maxbattery(const mobile *ptr3,int a){
    const mobile *carr=ptr3;
    int maxx= carr->batterycapacity;
    carr++;
    for(int i = 1; i<a; i++){
            if(carr->batterycapacity > maxx)
                maxx= carr->batterycapacity;
                carr++;}
                printf("maxbattery of phone = %d\n",maxx);
            }
int maxcamera(const mobile *ptr3,int a){
    const mobile *carr=ptr3;
    int maxx= carr->camera;
    carr++;
    for(int i = 1; i<a; i++){
            if(carr->camera > maxx)
                maxx= carr->camera;
                carr++;}
                printf("max camera resolution = %d",maxx);
}
