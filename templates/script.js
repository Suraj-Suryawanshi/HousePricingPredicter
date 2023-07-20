var tl = gsap.timeline()

        let x1=170
        let x2=-170
        let del=0
        
        tl
        .from("#na",{
            delay:1,
            y:-80
        }).to("#icon2",{
            duration:2,
            y:405
        })
        .from("#part1",{
            delay:del,
            x:x1,
            opacity:0
        }).from("#part2",{
            delay:del,
            x:x2,
            opacity:0
        }).from("#part3",{
            delay:del,
            x:x1,
            opacity:0
        }).from("#part11",{
            delay:del,
            x:x1,
            opacity:0
        }).from("#part4",{
            delay:del,
            x:x2,
            opacity:0
        }).from("#part5",{
            delay:del,
            x:x1,
            opacity:0
        }).from("#part6",{
            delay:del,
            x:x2,
            opacity:0
        }).from("#part7",{
            delay:del,
            x:x1,
            opacity:0
        }).from("#part8",{
            delay:del,
            x:x2,
            opacity:0
        }).from("#part9",{
            delay:del,
            x:x1,
            opacity:0
        }).from("#part10",{
            delay:del,
            x:x2,
            opacity:0
        }).from("#para",{
            delay:del,
            x:-150,
            opacity:0
        }).from("#ans",{
            delay:del,
            x:150,
            opacity:0
        }).from("#na>#Predict",{
            opacity:0,
            onStart: function(){
                $('#na>#Predict').textillate({ 
                    in: { 
                        effect: 'fadeInUp',
                        reverse:true,
                        
                        callback:function(){
                           
                        }
        
                        }
                });
            }
        }).from("#na>#About",{
            opacity:0,
            onStart: function(){
                $('#na>#About').textillate({ 
                    in: { 
                        effect: 'fadeInUp',
                        reverse:true,
                        
                        callback:function(){
                           
                        }
        
                        }
                });
            }
        })
        
        
        
        
        gsap.from("form",{
            y:500,
            duration:0.5
        })