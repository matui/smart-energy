const csvFilePath='./csv/power/103_PowerSum.csv'
const csv=require('csvtojson')
function parse_csv(file,name,output,cb){
  csv()
  .fromFile(file)
  .on('json',(jsonObj)=>{
     if(!jsonObj["1"] || jsonObj["1"]==0)
       return
     if(!output[jsonObj["CODE3"]])
       output[jsonObj["CODE3"]]={"Region":jsonObj["CODE3"],"County":jsonObj["COUN_NA"],"Town":jsonObj["TOWN_NA"]}
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
function parse_fac(file,name,output,cb){
  csv()
  .fromFile(file)
  .on('json',(jsonObj)=>{
     if(!jsonObj["102"])
       return
     if(!output[jsonObj["CODE3"]])
       return
     output[jsonObj["CODE3"]][name+"102"]=jsonObj["102"]
     output[jsonObj["CODE3"]][name+"103"]=jsonObj["103"]
     output[jsonObj["CODE3"]][name+"104"]=jsonObj["104"]
  })
  .on('done',(error)=>{
      cb(output)
  })
}
parse_csv('./csv/power/102_PowerSum.csv',"102_",[],(output)=>{
  parse_csv('./csv/power/103_PowerSum.csv',"103_",output,(output)=>{
    parse_csv('./csv/power/104_PowerSum.csv',"104_",output,(output)=>{
      parse_fac('./csv/factory/101_104_FactoryCount.csv',"Factory_cnt_",output,(output)=>{
        parse_fac('./csv/factory/101_104_FactoryEmployee.csv',"Factory_employee_",output,(output)=>{
          parse_fac('./csv/factory/101_104_FactoryTurnover.csv',"Factory_to_",output,(output)=>{
            parse_fac('./csv/factory/101_104_Turnover_Employee.csv',"To_employee_",output,(output)=>{
              parse_fac('./csv/factory/101_104_Turnover_Factory.csv',"To_factory_",output,(ou)=>{
                let title=""
                let flag =true
                for(var a in ou){
                  let ln = ""
                  if (Object.keys(ou[a]).length!=54)
                    continue
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
        })
      })
    })
  })
})
