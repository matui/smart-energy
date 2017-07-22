const csvFilePath='./csv/power/103_PowerSum.csv'
const csv=require('csvtojson')
function parse_csv(file,name,output,cb){
  csv()
  .fromFile(csvFilePath)
  .on('json',(jsonObj)=>{
     if(!jsonObj["1"] || jsonObj["1"]==0)
       return
     if(!output[jsonObj["CODE3"]])
       output[jsonObj["CODE3"]]={"Region":jsonObj["CODE3"]}
     output[jsonObj["CODE3"]][name+"1"]=jsonObj["1"]
     output[jsonObj["CODE3"]][name+"2"]=jsonObj["2"]
     output[jsonObj["CODE3"]][name+"3"]=jsonObj["3"]
     output[jsonObj["CODE3"]][name+"4"]=jsonObj["4"]
     output[jsonObj["CODE3"]][name+"5"]=jsonObj["5"]
     output[jsonObj["CODE3"]][name+"6"]=jsonObj["6"]
     output[jsonObj["CODE3"]][name+"7"]=jsonObj["7"]
     output[jsonObj["CODE3"]][name+"8"]=jsonObj["8"]
     output[jsonObj["CODE3"]][name+"9"]=jsonObj["9"]
     output[jsonObj["CODE3"]][name+"10"]=jsonObj["10"]
     output[jsonObj["CODE3"]][name+"11"]=jsonObj["11"]
     output[jsonObj["CODE3"]][name+"12"]=jsonObj["12"]
  })
  .on('done',(error)=>{
      cb(output)
  })
}
parse_csv('./csv/power/102_PowerSum.csv',"102_",[],(output)=>{
  parse_csv('./csv/power/103_PowerSum.csv',"103_",output,(out)=>{
    parse_csv('./csv/power/104_PowerSum.csv',"104_",out,(ou)=>{
      let title=""
      let flag =true
      for(var a in ou){
        let ln = ""
        for(var s in ou[a]){
          if(flag)
            title+=s+','
          ln += ou[a][s] + ','
        }
        console.log(ln)
        flag=false
      }
      console.log(title)
    })
  })
})
