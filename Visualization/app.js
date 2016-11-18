var width = 850
var height = 500

var svg = d3.select('svg')
    .attr('width', width)
    .attr('height', height)

d3.csv('athletes_sochi.csv', function(data){
  
     console.log(data)
     
     function maleSum(arr){
            var somma = d3.sum(arr,function(d,i){
                return (d.gender == 'Male')?1:0
            })
            return somma
        }
        
        function femaleSum(arr){
            var somma = d3.sum(arr,function(d,i){
                return (d.gender == 'Female')?1:0
            })
            return somma
        }

        //Funzione per definire il layout dell'arc
        var myPie = d3.layout.pie()
            .value(function(d){
                return d.m
            })

        var newdata = d3.nest()
            .key (function(d){
                return d.sport
            })
            .rollup(function(d){
                return { gender:[{m:maleSum(d), t:d.length, c:"blue"}, {m:femaleSum(d), t:d.length,c:"red"}]    
                        }
            })
            .entries(data)
        
        var min = 0
        var max =  d3.max(newdata,function(d,i){
            return d.values.gender[0].t 
        })
        var myScale = d3.scale.linear()
                   .domain([min,max*15])
                   .range([0,850])
        console.log(newdata)
        
        var myGroups = d3.select('svg')
        	.selectAll('g')
        	.data(newdata)
        	.enter()
        	.append('g')
        	.attr('transform',function(d,i){
                var y = ((i % 5)+1) * (450/5)
                var x = ((i % 3)) * (850/3) +100
                return 'translate('+ x +','+ y + ')'
			})
            
            myGroups.append('text')
                .text(function(d,i){
                    return d.key    
                })
                .attr('text-anchor', 'left')
                .attr('x', function(d,i){
                     return myScale((d.values.gender[0].t))+10
                })
                .attr('y', 0)
                .attr('font-family', 'arial')
                .attr('font-size',  14)
            
            //Creiamo la funzione myArc per dare la configurazione dell'arco
            var myArc= d3.svg.arc()
                .innerRadius(0)
                .outerRadius(function(d){
                    return myScale(d.data.t)//numeroAtleti// d.values.totale il valore tornato è dammi
                })
            
            //creaiamo la piechart
            myGroups.append('g')
                .selectAll('path')
                .data(function(d,i){
                    return myPie(d.values.gender) //definre MyPie  
                })
                .enter()
                .append('path')
                .attr('d', function(d,i){
                    //vai a recuperare il numero di atleti e passalo a myARc
                    return myArc(d)
                })
                .attr('fill', function(d,i){
                    return d.data.c
                })
           
//           
//           .append('text')
//           .text(function(d,i){
//                 return d.data.m
//                 })
//           .attr('opacity', 0)
//           .on('mouseenter', function(d,i){
//               d3.select(this)
//               .select('text')
//            .attr('opacity', 1)
//               
//           })
           
               
        
        
        
        
        
        
    
}) // chiusura del CVS