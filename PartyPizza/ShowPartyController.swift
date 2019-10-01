//
//  ShowPartyController.swift
//  PartyPizza
//
//  Created by nithin muthukumar on 2019-09-28.
//  Copyright © 2019 nithin muthukumar. All rights reserved.
//

import UIKit

class ShowPartyController: UIViewController {
    
    @IBOutlet weak var PartyField: UITextField!
    @IBAction func PartyChosen(_ sender: Any) {
        Globals.partyName=PartyField.text
        var dict=["command":"get_pizza_prefab_list","params":Globals.partyName!]
        var x=Commandler.makePost(dict)
        
        
    }
    override func viewDidLoad() {
        super.viewDidLoad()

        // Do any additional setup after loading the view.
    }
    

    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        // Get the new view controller using segue.destination.
        // Pass the selected object to the new view controller.
    }
    */

}
