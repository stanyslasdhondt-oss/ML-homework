import pickle

output_file = 'pipeline.bin'

with open(output_file,'rb') as f_load:
    model  = pickle.load(f_load)


lead = {
  "lead_source": "paid_ads",
  "industry": "technology",
  "employment_status": "employed",
  "location": "north_america",
  "number_of_courses_viewed": 2,
  "annual_income": 79276.0,
  "interaction_count": 4,
  "lead_score": 0.41
}
leads = [lead]

probability = model.predict_proba(leads)

print(probability[0][1].round(3))