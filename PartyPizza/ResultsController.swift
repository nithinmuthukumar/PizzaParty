//
//  ResultsController.swift
//  PartyPizza
//
//  Created by nithin muthukumar on 2019-09-29.
//  Copyright © 2019 nithin muthukumar. All rights reserved.
//

import UIKit
class ResultsController: UIViewController {
    @IBOutlet weak var LocationLabel: UILabel!
    @IBOutlet weak var PizzasLabel: UILabel!
    override func viewDidLoad() {
        super.viewDidLoad()
        //Commandler.makePost({"command":"get_pizza_list",["jalapeno"]})
        //LocationLabel.text=""
        PizzasLabel.text="Pizza 1: 4 jalapeno pizza 4 mushroom pizza"
        
        //2 people four slices
        //types of pizzas offered : Mushroom,Jalapeno and Olive,Pepperoni
        //ouput half is mushrooms half is jalapeno
        
        
        
       
    }
    

}
