//
//  CreatePizzaController.swift
//  PartyPizza
//
//  Created by nithin muthukumar on 2019-09-28.
//  Copyright © 2019 nithin muthukumar. All rights reserved.
//

import UIKit
//TODO: add button in table that shows ingredients
//also separate into vegetarian and non veg sections
class CreatePizzaController: UIViewController,UITableViewDelegate,UITableViewDataSource {
    @IBOutlet weak var TableView: UITableView!
    
    
    
    @IBAction func SubPizza(_ sender: Any) {
        Globals.pizzas.popLast()
        TableView.reloadData()
        
        
            
        
        
    }
    override func viewDidLoad() {
        super.viewDidLoad()
        TableView.delegate=self
        TableView.dataSource = self
        
            
        
    }
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return Globals.pizzas.count // your number of cells here
    }

    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell=tableView.dequeueReusableCell(withIdentifier: "Pizza",for: indexPath)
        // your cell coding

        cell.textLabel?.text=Globals.pizzas[indexPath.row].0
        
        return cell
    }
    override func viewDidAppear(_ animated: Bool) {
        super.viewDidAppear(animated)
//        //var ls=Globals.pizzas.map{(t:(String,[String:Bool])) in t.1}
//        var ls=["Hello"]
//        let indexPath=IndexPath.init(row: ls.count-1, section: 0)
//        TableView.beginUpdates()
//
//        TableView.insertRows(at: [indexPath], with: .automatic)
//        TableView.endUpdates()
 
 
    }

    @IBAction func HostParty(_ sender: Any) {
        var pizzas=[String:[String]]()
        for p in Globals.pizzas{
            pizzas[p.0]=p.1.keys.filter{k in p.1[k]!}
        }
        var newP=[[String:Any]]()
        for i in pizzas.keys{
            var dict=[String:Any]()
            dict["name"]=i
            dict["toppings"]=pizzas[i]
            newP.append(dict)
        }
        var message:[String:Any]=["command":"create_new_party","params":[Globals.partyName,newP]]
        Commandler.makePost(message)
    }
}
