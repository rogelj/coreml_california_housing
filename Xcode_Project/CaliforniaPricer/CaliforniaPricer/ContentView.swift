//
//  ContentView.swift
//  CaliforniaPricer
//
//  Created by J. Rogel onw 25/12/2025.
//

import SwiftUI
import CoreML

struct ContentView: View {
    let model = CaliforniaHousePricer()
    @State var popUpVisible: Bool = false
    @State var pickerIncome = 0
    @State var pickerRoom = 0
    let incomeData = Array(stride(from:0.05, through: 14, by: 0.5))
    let roomData = Array(2...10)
    
    var body: some View {
        VStack {
            Text("California Pricer").font(.largeTitle)
        }
        .padding()
        HStack(spacing: 40) {
            VStack(alignment: .leading) {
                Text("Income ($10k USD)")
                    .font(.caption)
                Picker(selection: $pickerIncome,
                       label: Text("Income")) {
                    ForEach(incomeData.indices, id: \.self) { ix in
                        Text("\(incomeData[ix], specifier: "%.2f")").tag(ix)
                    }
                }
            }
            VStack(alignment: .leading) {
                Text("No. Rooms")
                    .font(.caption)
                Picker(selection: $pickerRoom, label: Text("Rooms")) {
                    ForEach(roomData.indices, id: \.self) { ix in
                        Text("\(roomData[ix])").tag(ix)
                    }
                }
            }
        }
        .padding(.vertical, 40)
        Button(action: {
            self.popUpVisible.toggle()
        }) {
            Text("Get Prediction")
        }
        .alert(isPresented: self.$popUpVisible) {
            Alert(title: Text("Prediction"),
            message: Text("The values picked are\n Median Income: \(incomeData[pickerIncome])\n Avg No. Rooms: \(roomData[pickerRoom])"),
                  dismissButton: .default(Text("Cool!"))
            )
        }
    }
    
    func predictionMsg() -> String {
        let income = incomeData[pickerIncome]
        let rooms = Double(roomData[pickerRoom])
        
        guard let priceCalifornia = try? model.prediction(income: income, rooms: rooms) else {
            fatalError("Unexpected runtime error.")
        }
        
        let price = String(format: "%.2f", priceCalifornia.price*100000)
        let Msg = "Your property value is\n $\(price)"
        
        return Msg
    }
}

#Preview {
    ContentView()
}
